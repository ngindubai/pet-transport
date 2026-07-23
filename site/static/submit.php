<?php
/**
 * Pet Transport Global quote handler.
 *
 * Hostinger environment variables:
 *   PTG_RECIPIENT_EMAIL  mailbox that receives enquiry notifications
 *   PTG_CRM_API_KEY      server-side CRM credential (never expose in JavaScript)
 * Optional:
 *   PTG_CRM_ENDPOINT, PTG_SENDER_EMAIL, PTG_RATE_LIMIT_SALT
 */

declare(strict_types=1);

const SITE_URL = 'https://pettransportglobal.com';
const DEFAULT_RECIPIENT = 'info@pettransportglobal.com';
const DEFAULT_SENDER = 'noreply@pettransportglobal.com';
const DEFAULT_CRM_ENDPOINT = 'https://logistics-crm-tcu4.onrender.com/api/public/leads';

header('Cache-Control: no-store, max-age=0');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: strict-origin-when-cross-origin');

function redirect_to(string $path): void
{
    header('Location: ' . SITE_URL . $path, true, 303);
    exit;
}

function env_or_default(string $name, string $default): string
{
    $value = getenv($name);
    return is_string($value) && trim($value) !== '' ? trim($value) : $default;
}

function clean_text(?string $value, int $maxLength = 500): string
{
    $text = trim(strip_tags((string) $value));
    $text = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $text) ?? '';
    return function_exists('mb_substr')
        ? mb_substr($text, 0, $maxLength, 'UTF-8')
        : substr($text, 0, $maxLength);
}

function post_value(string $name, int $maxLength = 500): string
{
    $value = filter_input(INPUT_POST, $name, FILTER_UNSAFE_RAW);
    return clean_text(is_string($value) ? $value : '', $maxLength);
}

function rate_limit_exceeded(string $clientAddress): bool
{
    $salt = env_or_default('PTG_RATE_LIMIT_SALT', 'ptg-form-rate-limit-v1');
    $key = hash('sha256', $salt . '|' . $clientAddress);
    $file = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'ptg-' . $key . '.json';
    $now = time();
    $windowSeconds = 600;
    $maximumSubmissions = 5;

    $handle = @fopen($file, 'c+');
    if ($handle === false || !flock($handle, LOCK_EX)) {
        if (is_resource($handle)) {
            fclose($handle);
        }
        return false;
    }

    $raw = stream_get_contents($handle);
    $timestamps = json_decode($raw ?: '[]', true);
    if (!is_array($timestamps)) {
        $timestamps = [];
    }
    $timestamps = array_values(array_filter($timestamps, static function ($timestamp) use ($now, $windowSeconds): bool {
        return is_int($timestamp) && $timestamp > ($now - $windowSeconds);
    }));

    $blocked = count($timestamps) >= $maximumSubmissions;
    if (!$blocked) {
        $timestamps[] = $now;
        ftruncate($handle, 0);
        rewind($handle);
        fwrite($handle, json_encode($timestamps));
    }

    flock($handle, LOCK_UN);
    fclose($handle);
    return $blocked;
}

function send_to_crm(array $payload, string $idempotencyKey): bool
{
    $apiKey = getenv('PTG_CRM_API_KEY');
    if (!is_string($apiKey) || trim($apiKey) === '' || !function_exists('curl_init')) {
        return false;
    }

    $endpoint = env_or_default('PTG_CRM_ENDPOINT', DEFAULT_CRM_ENDPOINT);
    if (filter_var($endpoint, FILTER_VALIDATE_URL) === false) {
        return false;
    }

    $handle = curl_init($endpoint);
    curl_setopt_array($handle, [
        CURLOPT_POST => true,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CONNECTTIMEOUT => 3,
        CURLOPT_TIMEOUT => 8,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'X-API-Key: ' . trim($apiKey),
            'Idempotency-Key: ' . $idempotencyKey,
        ],
        CURLOPT_POSTFIELDS => json_encode($payload, JSON_UNESCAPED_SLASHES),
    ]);
    curl_exec($handle);
    $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
    $failed = curl_errno($handle) !== 0;
    curl_close($handle);
    return !$failed && $status >= 200 && $status < 300;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    redirect_to('/');
}

$honeypot = post_value('website', 100);
$startedAt = filter_input(INPUT_POST, 'form_started_at', FILTER_VALIDATE_INT);
$submittedTooQuickly = is_int($startedAt) && $startedAt > 0 && (time() - $startedAt) < 2;
$clientAddress = clean_text($_SERVER['REMOTE_ADDR'] ?? 'unknown', 64);

if ($honeypot !== '' || $submittedTooQuickly || rate_limit_exceeded($clientAddress)) {
    redirect_to('/thank-you/');
}

$name = post_value('name', 120);
$phone = post_value('phone', 60);
$emailInput = filter_input(INPUT_POST, 'email', FILTER_UNSAFE_RAW);
$email = filter_var(is_string($emailInput) ? trim($emailInput) : '', FILTER_VALIDATE_EMAIL);
$origin = strtoupper(post_value('origin_country', 2));
$destination = strtoupper(post_value('destination_country', 2));
$petType = strtolower(post_value('pet_type', 20));
$breed = post_value('breed', 120);
$weight = post_value('pet_weight_kg', 10);
$travelDate = post_value('travel_date', 10);
$message = post_value('message', 3000);
$landingPage = post_value('landing_page', 1000);

$validCountry = static function (string $value): bool {
    return preg_match('/^[A-Z]{2}$/', $value) === 1;
};
$validPetTypes = ['dog', 'cat', 'other'];

if (
    $name === '' || $email === false || $phone === '' ||
    !$validCountry($origin) || !$validCountry($destination) ||
    !in_array($petType, $validPetTypes, true)
) {
    redirect_to('/?form_error=missing_fields#quote-form');
}

$utm = [];
foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'] as $field) {
    $value = post_value($field, 200);
    if ($value !== '') {
        $utm[$field] = $value;
    }
}

$idempotencyKey = hash('sha256', strtolower((string) $email) . '|' . $origin . '|' . $destination . '|' . gmdate('Y-m-d-H'));
$crmPayload = array_merge([
    'company' => 'pet-transport',
    'name' => $name,
    'email' => $email,
    'phone' => $phone,
    'source' => 'Pet Transport Global website',
    'landing_page' => $landingPage,
    'message' => $message !== '' ? $message : null,
    'fields' => [
        'originCountry' => $origin,
        'destCountry' => $destination,
        'petType' => $petType,
        'breed' => $breed !== '' ? $breed : null,
        'weight' => $weight !== '' ? $weight : null,
        'travelDate' => $travelDate !== '' ? $travelDate : null,
    ],
], $utm);

$crmSent = send_to_crm($crmPayload, $idempotencyKey);

$routeHint = $origin . ' to ' . $destination;
$subject = 'Pet transport enquiry: ' . $routeHint . ' (' . $petType . ')';
$body = "New enquiry from pettransportglobal.com\n";
$body .= str_repeat('-', 50) . "\n\n";
$body .= "CONTACT DETAILS\nName: {$name}\nEmail: {$email}\nPhone: {$phone}\n\n";
$body .= "JOURNEY DETAILS\nOrigin: {$origin}\nDestination: {$destination}\n";
$body .= "Pet type: {$petType}\nBreed: {$breed}\nWeight (kg): {$weight}\nTravel date: {$travelDate}\n\n";
$body .= "NOTES\n" . ($message !== '' ? $message : '(none)') . "\n\n";
$body .= 'Submitted: ' . gmdate('Y-m-d H:i:s') . " UTC\n";

$recipient = env_or_default('PTG_RECIPIENT_EMAIL', DEFAULT_RECIPIENT);
$sender = env_or_default('PTG_SENDER_EMAIL', DEFAULT_SENDER);
$headers = "From: Pet Transport Global <{$sender}>\r\n";
$headers .= "Reply-To: {$email}\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "MIME-Version: 1.0\r\n";

$mailSent = filter_var($recipient, FILTER_VALIDATE_EMAIL) !== false
    && filter_var($sender, FILTER_VALIDATE_EMAIL) !== false
    && mail($recipient, $subject, $body, $headers);

if ($crmSent || $mailSent) {
    redirect_to('/thank-you/?submitted=1');
}

redirect_to('/?form_error=send_failed#quote-form');

<?php
/**
 * PetTransportGlobal - Quote Form Handler
 * Validates submission, sends email notification, redirects to thank-you page.
 *
 * NOTE FOR HOSTINGER SETUP:
 * PHP mail() should work on Hostinger shared hosting.
 * If emails land in spam, log in to Hostinger hPanel and configure the
 * email account noreply@pettransportglobal.com, or change SENDER_EMAIL
 * below to a verified Hostinger mailbox on your domain.
 */

define('RECIPIENT_EMAIL', 'garethsomers@outlook.com');
define('SENDER_EMAIL',    'noreply@pettransportglobal.com');
define('SITE_URL',        'https://pettransportglobal.com');

// Only handle POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ' . SITE_URL . '/');
    exit;
}

// ---- Honeypot check (bots fill the hidden "website" field) ----
$honeypot = isset($_POST['website']) ? trim($_POST['website']) : '';
if ($honeypot !== '') {
    // Silently redirect as if successful — do not alert the bot
    header('Location: ' . SITE_URL . '/thank-you/');
    exit;
}

// ---- Helper: sanitize plain text input ----
function sanitize_text(string $value): string {
    return htmlspecialchars(strip_tags(trim($value)), ENT_QUOTES, 'UTF-8');
}

// ---- Collect and validate inputs ----
$name     = sanitize_text(filter_input(INPUT_POST, 'name',    FILTER_DEFAULT) ?? '');
$phone    = sanitize_text(filter_input(INPUT_POST, 'phone',   FILTER_DEFAULT) ?? '');
$email    = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
$origin   = sanitize_text(filter_input(INPUT_POST, 'origin_country',      FILTER_DEFAULT) ?? '');
$dest     = sanitize_text(filter_input(INPUT_POST, 'destination_country', FILTER_DEFAULT) ?? '');
$pet_type = sanitize_text(filter_input(INPUT_POST, 'pet_type',     FILTER_DEFAULT) ?? '');
$breed    = sanitize_text(filter_input(INPUT_POST, 'breed',        FILTER_DEFAULT) ?? '');
$weight   = sanitize_text(filter_input(INPUT_POST, 'pet_weight_kg',FILTER_DEFAULT) ?? '');
$travel   = sanitize_text(filter_input(INPUT_POST, 'travel_date',  FILTER_DEFAULT) ?? '');
$message  = sanitize_text(filter_input(INPUT_POST, 'message',      FILTER_DEFAULT) ?? '');

// Required fields: name, email, phone
if (empty($name) || !$email || empty($phone)) {
    header('Location: ' . SITE_URL . '/?form_error=missing_fields#quote-form');
    exit;
}

// ---- Build email subject ----
$route_hint = ($origin && $dest) ? "{$origin} to {$dest}" : 'route not specified';
$subject = "Pet transport enquiry: {$route_hint}";
if ($pet_type) {
    $subject .= " ({$pet_type})";
}

// ---- Build plain-text email body ----
$body  = "New enquiry from PetTransportGlobal.com\n";
$body .= str_repeat('-', 50) . "\n\n";
$body .= "CONTACT DETAILS\n";
$body .= "Name:           {$name}\n";
$body .= "Email:          {$email}\n";
$body .= "Phone:          {$phone}\n\n";
$body .= "JOURNEY DETAILS\n";
$body .= "Origin:         {$origin}\n";
$body .= "Destination:    {$dest}\n";
$body .= "Pet type:       {$pet_type}\n";
$body .= "Breed:          {$breed}\n";
$body .= "Weight (kg):    {$weight}\n";
$body .= "Travel date:    {$travel}\n\n";
$body .= "NOTES\n";
$body .= $message ? $message : '(none)';
$body .= "\n\n" . str_repeat('-', 50) . "\n";
$body .= "Submitted: " . gmdate('Y-m-d H:i:s') . " UTC\n";
$body .= "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";

// ---- Email headers (prevent header injection — all values already sanitized) ----
$headers  = "From: Pet Transport Global <" . SENDER_EMAIL . ">\r\n";
$headers .= "Reply-To: {$email}\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "MIME-Version: 1.0\r\n";

// ---- Send ----
$sent = mail(RECIPIENT_EMAIL, $subject, $body, $headers);

if ($sent) {
    header('Location: ' . SITE_URL . '/thank-you/');
} else {
    // Mail failed — redirect back with error flag so user can try again
    header('Location: ' . SITE_URL . '/?form_error=send_failed#quote-form');
}
exit;

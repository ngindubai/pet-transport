<?php

/*
Template Name: United Pets
Author: Ingrid Kuhn
Author URI: themeforest/user/ingridk
*/

//Import PHPMailer class into the global namespace
use PHPMailer\PHPMailer\PHPMailer;

//Don't run this unless we're handling a form submission
if (array_key_exists('email', $_POST)) {
    date_default_timezone_set('Etc/UTC');
    require_once "../vendor/PHPMailer/PHPMailer.php";
    require_once "../vendor/PHPMailer/SMTP.php";
    require_once "../vendor/PHPMailer/Exception.php";
    $isAjax = !empty($_SERVER['HTTP_X_REQUESTED_WITH']) &&
    strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest';

    $mail = new PHPMailer();
	
		$mail->isSMTP();

		$mail->SMTPDebug = 0;
		$mail->Debugoutput = 'html';

		//your SMTP server (Change here)
		$mail->Host = "smtp.yoursmtp.com";

		//Set the SMTP port number - likely to be 25, 465 or 587 (Change here)
		$mail->Port = 587;

		//open tls if you use as like for gmail
		//$email->SMTPSecure = 'tls';
		//Whether to use SMTP authentication

		$mail->SMTPAuth = true;

		//Username to use for SMTP authentication (Change here)
		$mail->Username = "username";

		//Password to use for SMTP authentication (Change here)
		$mail->Password = "password";

		//Use a fixed address in your own domain as the from address
		//**DO NOT** use the submitter's address here as it will be forgery
		//and will cause your messages to fail SPF checks
		$mail->setFrom('youremail@yoursite.com', 'Your Site Name');

		//Choose who the message should be sent to
		$mail->addAddress("youremail@email.com");
   
   
    if ($mail->addReplyTo($_POST['email'], $_POST['name'])) {
        $mail->Subject = 'Contact form from your site';
        //Simple email without HTML
        $mail->isHTML(false);
        //Build a simple message body
        $mail->Body = <<<EOT
		Email: {$_POST['email']}
		Name: {$_POST['name']}
		Subject: {$_POST['subject']}
		Message: {$_POST['message']}
		EOT;
        //Send the message, check for errors	

         if (!$mail->send()) {
            
            $response = [
                'status'=> 1,
            ];
        } else {
            $response = [
                'status'=> 0,
            ];
        }
    } 

    if ($isAjax) {
        header('Content-type:application/json;charset=utf-8');
        echo json_encode($response);
        exit();
    }
}
?>
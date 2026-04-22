/*
Template Name: United Pets
Author: Ingrid Kuhn
Author URI: themeforest/user/ingridk
*/
"use strict";
jQuery(document).ready(function($) {
	
    $("#submit_btn").on("click", function() {
		
		//spinner
		$('#spinner-form').css('display','inline-block');
		
        var proceed = true;
        //simple validation at client's end
        //loop through each field and we simply change border color to red for invalid fields		
        $("#contact_form input[required], #contact_form textarea[required]").each(function() {
            $(this).css('background-color', '');
            if (!$.trim($(this).val())) { //if this field is empty 
                $(this).css('background-color', 'rgb(255 222 222 / 31%)'); //change border color to rgb(255 222 222 / 21%)   
                proceed = false; //set do not proceed flag
				 $("#spinner-form").hide();
					document.getElementById('contact_results').innerHTML = '<div class="alert alert-danger mt-4">Please fill all the required fields</div>';
            }
            //check invalid email
            var email_reg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
            if ($(this).attr("type") === "email" && !email_reg.test($.trim($(this).val()))) {
                $(this).css('background-color', 'rgb(255 222 222 / 31%)'); //change border color to rgb(255 222 222 / 21%)   
                proceed = false; //set do not proceed flag	
				 $("#spinner-form").hide();
				document.getElementById('contact_results').innerHTML = '<div class="alert alert-danger mt-4">Please enter a valid email</div>';			
            }
        });

        if (proceed) //everything looks good! proceed...
        {
            //get input field values data to be sent to server
            var post_data = {
                'name': $('input[name=name]').val(),
                'email': $('input[name=email]').val(),
				'subject': $('input[name=subject]').val(),
                'message': $('textarea[name=message]').val()
            };

            //Ajax post data to server
            $.post('php/sendmail.php', post_data, function(response) {
                if (response.status == 1) { //load json data from server and output message     
                    var output = '<div class="alert alert-danger mt-4"><i class="fas fa-circle-exclamation text-danger"></i>Could not send mail! Please check your mail configuration.</div>';
					 $("#error-message,#spinner-form").hide();
                } else {
                    var output = '<div class="alert alert-success mt-4" role="alert"><i class="fas fa-check-circle text-success"></i>Thank you for your message. We will contact you soon.</div>';
                    //reset values in all input fields and hide error
                    $("#contact_form input, #contact_form textarea").val('');
					 $("#error-message,#spinner-form").hide();

                }
			
                $("#contact_results").hide().html(output).slideDown();
            }, 'json');
        }
    });

    
});

 
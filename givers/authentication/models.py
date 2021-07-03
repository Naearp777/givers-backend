from django.core.mail.message import EmailMultiAlternatives
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.template.loader import render_to_string

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "There was a request to change your password! If you did not make this request then please ignore this email. {}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    email_html_message =render_to_string('email_send.html')
    print(reset_password_token.key)
    res = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Volunteer Management System"),
        # message:
        email_html_message,
        # from:
        "admin@volunteermanagementsystem.com",
        # to:
        [reset_password_token.user.email]
    )
    res.content_subtype = "html"  # Main content is now text/html
    res.send()
    
    
    
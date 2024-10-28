from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    emailSubject = "Your account needs to verified"
    emailFrom = settings.EMAIL_HOST_USER
    emailMessage = f"Hi, Click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}"
    print("EMAIlFROM--"+emailFrom)
    print("EMAIl--"+email)

    send_mail(emailSubject, emailMessage, emailFrom, [email],  fail_silently=False,auth_user=None, auth_password=None, connection=None, html_message=None)
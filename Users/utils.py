from django.conf import settings
from django.core.mail import send_mail
import random

from .models import OtpData
from django.contrib.auth import get_user_model
User=get_user_model()


def send_otp_email(user_name: str, user_email: str, OTP: int | str) -> int:   

    message_content = f"""Dear {user_name},
        Your code for ApexSky Projects Management is: 
        CODE: {OTP}
        
        Keep it private and do not share it.
        If this request was not made by you, simply ignore this email.

        Well Wishes,
        Developer Sami(APEXSKY)
        """
    print("-----------Hello from send_otp_email, Sending.......")
    send_mail(
        subject= "[Development OTP] ApexSky Sign-in code",
        message=message_content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list= [user_email],
        fail_silently= False
    )
    return

# To generate OTP for Verification.
def send_otp_code(user_email: str, username: str):
    OTP = str(random.randint(111111, 999999))
    
    OtpData.objects.update_or_create(email = user_email,defaults={'otp':OTP})
    send_otp_email(username, user_email, OTP)


# To hide unique part of email 
def hide_and_seek_email(user_email: str) -> str:
    
    secure_email = user_email
    
    return secure_email


# Split the email first part for temp username.
def username_extract(email: str) -> str:
    username = email.split('@')[0]
    
    return username
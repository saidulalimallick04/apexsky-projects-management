from django.conf import settings
import random
import smtplib
from email.message import EmailMessage

from django.contrib.auth import get_user_model
User=get_user_model()


def send_otp_email(request):    
    otp=''
    for i in range(6):
        otp+=str(random.randint(0,9))
        
    User.objects.filter(email=request.user.email).update(user_ott=otp)
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    ourEmail=settings.EMAIL_HOST_USER
    ourPass=settings.EMAIL_HOST_PASSWORD
    server.login(ourEmail,ourPass)
    
    msg=EmailMessage()
    
    msg['Subject']= 'OTP Verification'
    
    msg['From']= ourEmail
    
    msg['To']= request.user.email
    
    msg.set_content(f"""\
                    Dear {request.user.first_name},

                    Your code for Sami's Projects is: 

                    🔢 {otp}

                    Keep it private and do not share it.

                    If this request was not made by you, simply ignore this email.

                    Best,  
                    Samis'Project
                    """)
    
    server.send_message(msg)
    return "Check Your Mail!!"
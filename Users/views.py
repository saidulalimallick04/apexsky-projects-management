from .utils import *
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Projects.models import ProjectDetail

from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.

def createAccount(request):
    
    if request.method=='POST':
        if 'AccountCreate' in request.POST:
            try:
                data=request.POST
                
                First_Name=data.get('First_Name')
                Last_Name=data.get('Last_Name')
                
                Email=data.get("Email")
                Password=data.get("Password")
                
                About_Me=data.get('About_Me')
                Phone_Number=data.get('Phone_Number')
                
                Location=data.get('Location')
                DoB=data.get('DoB')
                Gender=data.get("Gender")
                
                user=User.objects.create(
                    email=Email,
                    first_name=First_Name,
                    last_name=Last_Name, 
                    about_me=About_Me,
                    phone_number=Phone_Number,
                    location=Location,
                    gender=Gender,
                    date_of_birth=DoB
                )
                user.set_password(Password)
                user.save()
                
                messages.info(request,"Account Created Successfully ^_^")
                return redirect("/login")
            except:
                messages.info(request, "Something Went wrong!!")
                return redirect("/createaccount")
    else:     
        return render(request,"users/create_Account_page.html")
    
@login_required(login_url='/login/')
def setNickname(request):
    if request.method=="POST":
        auth_user=request.user
        print(auth_user)
        
        data=request.POST
        user_nickname=data.get("Nickname")
        
        if User.objects.filter(nickname=user_nickname).exists():
            messages.error(request,"Nickname already used!!")
            return redirect("/setnickname")
        else:
            try:
                user1=User.objects.get(id=auth_user.id)
                user1.nickname=user_nickname
                user1.save()
                
                ProjectDetail.objects.filter(user=request.user.id).update(nickname=user_nickname)
                
                messages.info(request,"Nickname set successfully ^_^")
                
                return redirect('/profile')
            except:
                messages.error(request,"Something went wrong!!")
                return redirect("/setnickname")
    else:
        return render(request, 'users/set_nickname_page.html')

#-----------------------------------------------------------------------------------------------------------------------------------------
def loginAccount(request):
    
    next_url=request.GET.get('next','/')
    
    if request.method=='POST':
        data=request.POST
        
        Email=data.get('Email')
        Password=data.get('Password')
        
        is_user=User.objects.filter(email=Email)
        
        if is_user is None:
            messages.warning(request,"No User Found!!")
            return redirect("/login/")
        else:
            user=authenticate(email=Email,password=Password)
            
            if user is not None:
                login(request,user)
                messages.info(request,"Login Successful ^_^")
                return redirect(next_url)
            else:
                messages.info( request,"Invalid Details!!")
                return redirect ("/login/")
            
    return render(request, 'users/Login_page.html')

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def logoutAccount(request):
    
    logout(request)
    messages.info(request,"Logout!!")
    
    return redirect("/home")

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def userDashboard(request):
    
    return render(request, 'users/dashboard_Page.html')

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def userProfile(request):
    
    if request.user.is_verified ==0:
        messages.info(request,"Please Verify Your Email!!\nOtherwise After 356 Days your account will be deleted Permanently(From Last Login)")
        
    return render(request, 'users/profile_page.html')

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def verifyEmail(request):
    
    if request.user.is_verified:
        return redirect('/profile')
    
    if request.method=="POST":
        if 'SendEmail' in request.POST:
            try: 
                messages.info(request,send_otp_email(request))
                return redirect('/otpconformation/')
            except:
                messages.info(request, "Something wrong!!")
            
    return render(request, 'users/verify_email_page.html')


#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def otpConformation(request):
    
    if 'OTP_SUBMISSION' in request.POST:
        data=request.POST

        userInput=data.get('OTP')
        otp=User.objects.get(email=request.user.email).user_ott
        
        if otp==userInput:
            User.objects.filter(email=request.user.email).update(is_verified=True)
            User.objects.filter(email=request.user.email).update(user_ott='')
            messages.info(request, "Verified ^_^")
            return redirect('/profile/')
        else:
            messages.info(request, "Invaild OTP")
            return render(request, 'users/verify_email_page.html')
                
    return render(request,'users/otp_conformation_page.html')

@login_required(login_url='/login/')
def updateProfile(request):
    
    if request.method=="POST":
        try:
            data=request.POST
            uuid=request.user.unique_identifier
            First_Name=data.get('First_Name')
            Last_Name=data.get('Last_Name')

            About_Me=data.get('About_Me')
            Phone_Number=data.get('Phone_Number')
            Location=data.get('Location')
            DoB=data.get('DoB')
            Gender=data.get("Gender")

            user1=User.objects.get(unique_identifier=uuid)
            user1.first_name=First_Name
            user1.last_name=Last_Name
            user1.about_me=About_Me
            user1.phone_number=Phone_Number
            user1.location=Location
            user1.gender=Gender
            user1.date_of_birth=DoB
            user1.save()
            
            messages.info(request," Update Successful ^_^")
            
            return redirect("/profile")
            
        except:
            messages.info(request, "Something Went wrong!!")
            return redirect("/updateprofile")
    else:
        
        
        return render(request,'users/edit_profile_page.html')

@login_required(login_url='/login/')
def deleteProfile(request):
    
    try:    
        User.objects.get(email=request.user.email).delete()
        messages.info(request, "Deleted")
    except:
        messages.info(request,"Already Deleted")    
    return redirect("/")
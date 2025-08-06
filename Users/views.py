from django.shortcuts import render,redirect,resolve_url
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.db.models import Count

from django.contrib.auth import get_user_model
from Projects.models import Project
# Create your views here.

User=get_user_model()

#--------------------------------------------------------------------------------------------------------------------------------
def login_account(request):
    """
        This Function is for Login Page.\n
        Context Values: [  ]
    """
    next_url=request.GET.get('next','/')
    print(next_url)
    if request.method=='POST':
        data=request.POST
        
        login_email=data.get('login_email_address')
        login_password=data.get('login_password')
        
        is_user=User.objects.filter(email=login_email)
        if is_user is None:
            messages.warning(request,"No User Found!!")
            return redirect(resolve_url("login-account"))
        
        user=authenticate(email=login_email,password=login_password)
        
        if user:
            login(request,user)
            messages.info(request,"Login Successful ^_^")
            return redirect(next_url)
        else:
            messages.info( request,"Invalid Details!!")
            return redirect (resolve_url("login-account"))
            
    return render(request, 'users/login_page.html')

# #-----------------------------------------------------------------------------------------------------------------------------------------

def create_account(request):
    """
        This function helps to Create User Account in ApexSky.\n
        Context Values: []
    """
    if request.method=='POST':
        try:
            data=request.POST
            
            new_user_nickname=data.get('nickname')
            new_user_email=data.get("email_address")
            new_user_password=data.get("password")
            
        except Exception as e:
            print("Error: ",e)
        
        print("\n----------Data Accepted----------\n")
        
        try:
            user=User.objects.create(
                email=new_user_email,
                username = new_user_nickname
            )
            user.set_password(new_user_password)
            user.save() # Account Created
            
            login(request=request,user=user)
            messages.info(request,"Account Created Successfully ^_^")
            return redirect(resolve_url("login-account"))
        except:
            messages.info(request, "Email/User already occupied.")
            return redirect(resolve_url("create-account-page"))
    else:     
        return render(request,"users/create_account_page.html")



# @login_required(login_url='/login/')
# def set_nickname(request):
#     if request.method=="POST":
#         auth_user=request.user
#         print(auth_user)
        
#         data=request.POST
#         user_nickname=data.get("Nickname")
        
#         if User.objects.filter(nickname=user_nickname).exists():
#             messages.error(request,"Nickname already used!!")
#             return redirect("/setnickname")
#         else:
#             try:
#                 user1=User.objects.get(id=auth_user.id)
#                 user1.nickname=user_nickname
#                 user1.save()
                
#                 Project.objects.filter(user=request.user.id).update(nickname=user_nickname)
                
#                 messages.info(request,"Nickname set successfully ^_^")
                
#                 return redirect('/profile')
#             except:
#                 messages.error(request,"Something went wrong!!")
#                 return redirect("/setnickname")
#     else:
#         return render(request, 'users/set_nickname_page.html')

# #-----------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def logout_account(request):
    """
        This function Remove/ Log-out the current authentication user.\n
        Context Values: []
    """
    logout(request)
    messages.info(request,"Logout!!")
    return redirect(resolve_url("landing-page"))

# #-----------------------------------------------------------------------------------------------------------------------------------------
# @login_required(login_url='/login/')
# def user_dashboard(request):
    
#     return render(request, 'users/dashboard_Page.html')

# #-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url="/login/")
def user_profile(request):
    """
        This finction is for User Profile Page.\n
        Context Values: []
    """
    userProjects = Project.objects.filter(user = request.user).order_by('?')[:4]
    total_project = Project.objects.filter(user = request.user)
    total_project_count = total_project.count()
    
    live_project_count = total_project.filter(status = "Live").count()
    verified_project_count = total_project.filter(is_verified = True).count()


    context = {
        'userProjects': userProjects,
        'total_project_count' : total_project_count,
        'live_project_count' : live_project_count,
        'verified_project_count' : verified_project_count,
    }
    return render(request, 'users/user_profile_page.html',context)

# #-----------------------------------------------------------------------------------------------------------------------------------------

def user_account(request):
    """
        This Function returns User Account Details Page.\n
        Context Values: []
    """
    return render(request,"users/user_account_page.html")


# #-----------------------------------------------------------------------------------------------------------------------------------------
# @login_required(login_url='/login/')
# def verify_email(request):
    
#     if request.user.is_verified:
#         return redirect('/profile')
    
#     if request.method == "POST":
#         if 'SendEmail' in request.POST:
#             try: 
#                 messages.info(request,send_otp_email(request))
#                 return redirect('/otpconformation/')
#             except:
#                 messages.info(request, "Something wrong!!")
            
#     return render(request, 'users/verify_email_page.html')

# def resetPassword(request):
    
#     return render(request,'users/otp_conformation_page.html')

# #-----------------------------------------------------------------------------------------------------------------------------------------
# @login_required(login_url='/login/')
# def otp_conformation(request):
    
#     if 'OTP_SUBMISSION' in request.POST:
#         data=request.POST

#         userInput=data.get('OTP')
#         otp=User.objects.get(email=request.user.email).user_ott
        
#         if otp==userInput:
#             User.objects.filter(email=request.user.email).update(is_verified=True)
#             User.objects.filter(email=request.user.email).update(user_ott='')
#             messages.info(request, "Verified ^_^")
#             return redirect('/profile/')
#         else:
#             messages.info(request, "Invaild OTP")
#             return render(request, 'users/verify_email_page.html')
                
#     return render(request,'users/otp_conformation_page.html')

# #--------------------------------------------------------------------------------------------------------------------------------
# @login_required(login_url='/login/')
# def update_profile(request):
    
#     if request.method=="POST":
#         try:
#             data=request.POST
#             uuid=request.user.unique_identifier
#             First_Name=data.get('First_Name')
#             Last_Name=data.get('Last_Name')

#             About_Me=data.get('About_Me')
#             Phone_Number=data.get('Phone_Number')
#             Location=data.get('Location')
#             DoB=data.get('DoB')
#             Gender=data.get("Gender")

#             user1=User.objects.get(unique_identifier=uuid)
#             user1.first_name=First_Name
#             user1.last_name=Last_Name
#             user1.about_me=About_Me
#             user1.phone_number=Phone_Number
#             user1.location=Location
#             user1.gender=Gender
#             user1.date_of_birth=DoB
#             user1.save()
            
#             messages.info(request," Update Successful ^_^")
            
#             return redirect("/profile")
            
#         except:
#             messages.info(request, "Something Went wrong!!")
#             return redirect("/updateprofile")
#     else:
        
        
#         return render(request,'users/edit_profile_page.html')

# #--------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url="/login/")
def delete_account(request):
    """
        Be sure!! This Function delete Current user's entire Details from database.
    """
    try:    
        User.objects.get(uid=request.user.uid).delete()
        messages.info(request, "Deleted")
    except:
        messages.info(request,"Already Deleted")    
    return redirect(resolve_url("landing-page"))
"""
URL configuration for ProjectRoot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from .views import *
from Home.views import *
from Users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #--------------------------------------------------------------------------
        # Home ---->>
    
    path("",home_page,name='landing-page'),
    path("search/",search_page,name='search-page'),
    path("explore/",explore_page,name='explore-page'),
    # path("aboutus/",aboutUsPage,name='Heavenly-Bytes-AboutUs'),
    # path("contactus/",contactUsPage,name='Heavenly-Bytes-ContactUs'),
    
    
    path("url-not-found/",urlNotFound,name='url-not-found'),
    #--------------------------------------------------------------------------
        # Users ---->>
    
    path("create-account/",createAccount,name="Create_Account"),
    path("login/",loginAccount,name="login-page"),
    path("logout/",logoutAccount,name="Logout"),
    path("profile/",userProfile,name='profile-page'),
    path("account/",user_account,name='user-account-page'),
    path("set-nickname/",setNickname,name='Set_Nickname'),
    path("update-profile/",updateProfile,name='Update_Profile'),
    path("delete-profile/",deleteProfile,name='Delete_Profile'),
    
    path("verify-email/",verifyEmail,name='Email_Varification_Page'),
    path("otp-conformation/",otpConformation,name='Email_OTP_Page'),
    
    #--------------------------------------------------------------------------
        # Projects ---->>
        
    path("projects/",include("Projects.urls")),
    

    #--------------------------------------------------------------------------
        # Blogs ---->>
        
    path("blogs/",include("Blogs.urls")),
    
    
    #--------------------------------------------------------------------------
        # APIs ---->>
        
    path("api/",include("API.urls"))
]




handler404=custom_404
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
    
    path("",homePage,name='Heavenly_Bytes'),
    path("home/",homePage,name='Heavenly_Bytes'),
    path("search/",searchData,name='SearchUrl'),
    # path("explore/",explorePage,name='Heavenly-Bytes-Explore'),
    # path("aboutus/",aboutUsPage,name='Heavenly-Bytes-AboutUs'),
    # path("contactus/",contactUsPage,name='Heavenly-Bytes-ContactUs'),
    
    
    
    path("url-not-found/",urlNotFound,name='UrlNotFound'),
    #--------------------------------------------------------------------------
        # Users ---->>
    
    path("createaccount/",createAccount,name="Create_Account"),
    path("login/",loginAccount,name="Login"),
    path("logout/",logoutAccount,name="Logout"),
    path("profile/",userProfile,name='Profile_Page'),
    path("setnickname/",setNickname,name='Set_Nickname'),
    path("updateprofile/",updateProfile,name='Update_Profile'),
    path("deleteprofile/",deleteProfile,name='Delete_Profile'),
    
    path("verifyemail/",verifyEmail,name='Email_Varification_Page'),
    path("otpconformation/",otpConformation,name='Email_OTP_Page'),
    
    
    #--------------------------------------------------------------------------
        # Projects ---->>
        
    path("projects/",include("Projects.urls")),
    
    
    
    #--------------------------------------------------------------------------
        # Projects ---->>
        
    path("blogs/",include("Blogs.urls"))
    
    
    
    
    
]




handler404=custom_404
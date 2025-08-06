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

from .views import custom_404,custom_500
from Home.views import home_page, explore_page, search_page, url_not_found
from Users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # #------------------------------------------------------------------------------------
    #     # Home ---->>
    path("",home_page,name='landing-page'),
    path("search/",search_page,name='search-page'),
    path("explore/",explore_page,name='explore-page'),
    # path("aboutus/",about_us,name='about-us_page'),
    # path("contactus/",contact_us,name='contact-us_page'),
    
    path("url-not-found/",url_not_found,name='url-not-found'),

    # --------------------------------------------------------------------------------------
    #Users ---->>
    
    path("create-account/",create_account,name="create-account-page"),
    path("login/",login_account,name="login-account"),
    path("logout/",logout_account,name="logout-account"),
    path("profile/",user_profile,name='profile-page'),
    path("account/",user_account,name='user-account-page'),
    # path("set-nickname/",set_nickname,name='set-nickname'),
    # path("update-profile/",update_profile,name='update-profile'),
    path("delete-account/",delete_account,name='delete-account'),
    
    # path("verify-email/",verifyEmail,name='Email_Varification_Page'),
    # path("otp-conformation/",otpConformation,name='Email_OTP_Page'),

    #----------------------------------------------------------------------------------------
    # Projects ---->>
    path("projects/",include("Projects.urls")),

    #----------------------------------------------------------------------------------------
    # Blogs ---->>
    # path("blogs/",include("Blogs.urls")),

    # #--------------------------------------------------------------------------------------
    # APIs ---->>
    # path("api/",include("API.urls"))
]

handler404=custom_404
handler500 = custom_500
from django.urls import path
from .views import *

urlpatterns=[
    path("",blogHomepage,name="Blog_Homepage")
]
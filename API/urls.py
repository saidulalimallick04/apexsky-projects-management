from django.urls import path
from .views import *

urlpatterns = [
    path('projects/<str:user_nickname>/',get_projects,name='Get_Projects')
]

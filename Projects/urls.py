
from django.urls import path,include

from .views import *

urlpatterns = [
    
    path("",projectsHome,name='Project_Home_Page'),
    path("allprojects/<int:category_id>/",allProjects,name='All_Projects'),
    path("projectoverview/<int:project_id>",ProjectOverview,name='Project_Overview'),
    path("registerproject/",registerProject,name="Register_Project"),
    path("myprojects/",myProjects,name='Dashboard_Page'),
    
    path("updateproject/<int:project_id>",updateProject,name="Update_Project")
]


from django.urls import path,include

from .views import *

urlpatterns = [
    
    path("",projectsHome,name='all-project-page'),
    path("allprojects/<int:category_id>/",allProjects,name='All_Projects'),
    path("projectoverview/<int:project_id>",ProjectOverview,name='Project_Overview'),
    
    path("new-project/",registerProject,name="new-project-page"),
    
    path("myprojects/",myProjects,name='Dashboard_Page'),
    
    path("updateproject/<int:project_id>",updateProject,name="Update_Project")
]

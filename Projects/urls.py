
from django.urls import path,include

from .views import *

urlpatterns = [
    
    path("", projects_home, name='project-homepage'),
    path("new-project/",create_new_project,name="new-project-page"),
    
    # path("allprojects/<int:category_id>/",allProjects,name='All_Projects'),
    # path("projectoverview/<int:project_id>",ProjectOverview,name='Project_Overview'),

    
    # path("myprojects/",myProjects,name='Dashboard_Page'),
    
    # path("updateproject/<int:project_id>",updateProject,name="Update_Project")
]

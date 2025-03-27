
from django.urls import path,include

from .views import *

urlpatterns = [
    
    path("",projectsHome,name='ProjectHomePage'),
    path("allprojects/<int:category_id>/",allProjects,name='AllProjects'),
    path("projectoverview/<int:project_id>",ProjectOverview,name='ProjectOverview'),
    path("registerproject/",registerProject,name="RegisterProject"),
    path("myprojects/",myProjects,name='MyProjects'),
    
    path("updateproject/<int:project_id>",updateProject,name="EditProject")
]

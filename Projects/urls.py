
from django.urls import path,include

from .views import *

urlpatterns = [
    
    path("", projects_home, name='project-homepage'),
    
    path("new-project/",create_new_project,name="new-project-page"),
    
    path("c/<str:catalog_handle>",all_projects,name='view-catalog'),
    path("l/<str:label_handle>",view_project,name='view-label'),
    path("p/<str:project_handle>",view_project,name='view-project'),
    
    # path("my-projects/",myProjects,name='Dashboard_Page'),
    
    # path("update-project/<int:project_handle>",updateProject,name="Update_Project")
]

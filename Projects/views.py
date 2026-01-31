from django.shortcuts import render,redirect,resolve_url
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Project,ProjectCatalog,ProjectLabel

# Create your views here.

User=get_user_model()

def projects_home(request):
    """
        This Function return Project Homepage.\n
        Carries Some of every projects. and can view all projects of that Catagory/Catalog.
    """
    # projects_demo_video = Project.objects.filter(demo_video is not None )

    projectCatalogs = ProjectCatalog.objects.order_by("?")
    
    context={
        'projectCatalogs': projectCatalogs
    }
    return render(request,'projects/project_homepage.html',context)


#--------------------------------------------------------------------------------------------------------------------------------
def all_projects(request,catalog_handle):
    
    """
    Descriprions:
    ------------
        This Function will return a http responce with multiple project of same catagory/catalog.
    Parameters:
        Request(httpRequest), catalog_handle
    """
    catalog_object=ProjectCatalog.objects.get(handle = catalog_handle)
    projects_QUERYSET=Project.objects.filter(catalog=catalog_object).order_by('-view_count')
    
    
    context={
        "Project_type": catalog_object.name,
        "projects": projects_QUERYSET
    }
    
    return render(request,'projects/see_all_projects_page.html',context)

#--------------------------------------------------------------------------------------------------------------------------------

def view_project(request,project_handle):
    """
        This Function will fetch one Project at a time to see the project.\n
        Context Values: [project]
    """
    reqested_project=Project.objects.get(handle = project_handle)
    
    reqested_project.view_count += 1
    reqested_project.save()

    
    
    reqested_Project_catalog = ProjectCatalog.objects.values_list("name", "handle").get(name = reqested_project.catalog)
    reqested_Project_label = ProjectLabel.objects.values_list("name", "handle").get(name = reqested_project.label)

    context={
        "project": reqested_project,
        "reqested_Project_catalog": reqested_Project_catalog,
        "reqested_Project_label": reqested_Project_label,
    }
    return render(request,'projects/view_project_page.html',context)

#--------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url="/login/")
def create_new_project(request):
    
    if request.method =="POST":
        try:
            data=request.POST

            project_thumbnail_image = request.FILES.get("project_image")
            project_document = request.FILES.get("project_document")

            project_name = data.get("project_name")
            project_status = data.get("project_status")
            project_content = data.get("project_content")
            user_username=request.user.username
            
            project_catalog_id = data.get("project_catalog_id")
            project_catalog = ProjectCatalog.objects.get(id=project_catalog_id)
            
            project_label_id = data.get("project_label_id")
            project_label = ProjectLabel.objects.get(id=project_label_id)
            
            deployed_url=data.get("deployed_url")
            demo_video = data.get("demo-video-url")
            github_url=data.get("github_url")
            
        except Exception as e:
            print("Error:", e)
            messages.error(request, e)
            return redirect(resolve_url('new-project-page'))
        try:
            new_project= Project()
            new_project.name= project_name
            new_project.status= project_status
            new_project.user_username= user_username
            
            new_project.user= request.user  
            new_project.catalog= project_catalog
            new_project.label= project_label

            # These Values are not required. 
            # So None can also come from frontend.
            if project_content:                         
                new_project.content= project_content
            if deployed_url:
                new_project.deployed_url= deployed_url
            if demo_video:
                new_project.demo_video = demo_video
            if github_url:
                new_project.github_repository = github_url

            new_project.thumbnail_image = project_thumbnail_image   # if None, No issue
            new_project.document_file = project_document            # if None, No issue

            new_project.save()
            
            messages.info(request, 'Register!! waiting for varification.')
            return redirect(resolve_url("profile-page"))
        
        except EOFError:
            messages.info(request, EOFError)
            
            return redirect(resolve_url("new-project-page"))
            
    else:
        catalog_QUERYSET=ProjectCatalog.objects.values_list("id", "name").all()
        label_QUSERSET=ProjectLabel.objects.values_list("id", "name",).all()
        
        context={
            'allCatalogs': catalog_QUERYSET,
            'allLabel': label_QUSERSET
        }
        return render(request,'projects/create_new_project_page.html',context)


#--------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url="/login/")
def update_project(request,project_handle):
    
    project_handle = project_handle
    
    if request.method=="POST":
        try:
            data = request.POST

            project_thumbnail_image = request.FILES.get("project_image")
            project_document = request.FILES.get("project_document")

            project_name = data.get("project_name")
            project_status = data.get("project_status")
            project_content = data.get("project_content")
            user_username=request.user.username
            
            project_catalog_id = data.get("project_catalog_id")
            project_catalog = ProjectCatalog.objects.get(id=project_catalog_id)
            
            project_label_id = data.get("project_label_id")
            project_label = ProjectLabel.objects.get(id=project_label_id)
            
            deployed_url=data.get("deployed_url")
            demo_video = data.get("demo-video-url")
            github_url=data.get("github_url")
        except:
            messages.warning(request=request, message="Server can't handle this request at this moment. Try again Later!!")
            return redirect(resolve_url("profile-page"))
        

        try:   
            new_project= Project.objects.get(handle = project_handle)
            new_project.name= project_name
            new_project.status= project_status
            new_project.user_username= user_username
            
            new_project.user= request.user  
            new_project.category= project_catalog
            new_project.label= project_label

            # These Values are not required. 
            # So None can also come from frontend.
            if project_content:                         
                new_project.content= project_content
            if deployed_url:
                new_project.deployed_url= deployed_url
            if demo_video:
                new_project.demo_video = demo_video
            if github_url:
                new_project.github_repository = github_url

            new_project.thumbnail_image = project_thumbnail_image   # if None, No issue
            new_project.document_file = project_document            # if None, No issue

            new_project.save()
            
            messages.info(request, 'Updated!!')

            return redirect('/projects/myprojects')
        except:
            messages.warning(request=request, message="Server can't handle this request at this moment. Try again Later!!")
            return redirect(resolve_url("profile-page"))
    else:

        project_QUERY=Project.objects.get(handle = project_handle)
        catalog_QUERYSET=ProjectCatalog.objects.values_list("id", "name").all()
        label_QUSERSET=ProjectLabel.objects.values_list("id", "name",).all()
        
        context={
            "project" : project_QUERY,
            'allCatalogs': catalog_QUERYSET,
            'allLabel': label_QUSERSET
        }
        return render(request,'projects/edit_project_page.html',context)

#--------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def current_user_projects(request):
    
    projects_QUERYSET=Project.objects.filter(user=request.user).order_by('-id')
    
    context={
        "projects": projects_QUERYSET
    }
    
    return render(request,'projects/see_my_projects_page.html',context)

#--------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def delete_project(request, project_handle):
    
    project_QUERY=Project.objects.get(handle = project_handle)
    
    messages.error(request=request , message=f"Project {project_QUERY.name} Deleted Successfully")
    
    return redirect(resolve_url("profile"))

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
def all_projects(request,category_handle):

    catalog_object=ProjectCatalog.objects.get(handle = category_handle)
    projects_QUERYSET=Project.objects.filter(catalog=catalog_object).order_by('-project_use_count')
    
    
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
    
    reqested_project.use_count += 1
    reqested_project.save()
    
    context={
        "project": reqested_project
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
            
            
        try:
            new_project= Project()
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
'''
#--------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url="/login/")
def updateProject(request,project_id):
    
    proj_id=project_id
    
    if request.method=="POST":
        
        data=request.POST
        
        Project_Name=data.get("Project_Name")
        Project_descriptions=data.get("About_Project")
        
        Project_Status=data.get("Status")
        Project_Category=data.get("Category")
        Project_Label=data.get("Label")
        Category_Object=ProjectCatalog.objects.get(category_name=Project_Category)
        Label_Object=ProjectLabel.objects.get(label_name=Project_Label)
        
        Project_Url=data.get("Project_Url")
        Project_Github_Repo=data.get("Github_Repository")
        
        
        project1=Project.objects.get(id=proj_id)
        
        project1.category=Category_Object
        project1.label=Label_Object
        project1.project_name=Project_Name
        project1.project_status=Project_Status
        
        if Project_descriptions != ""  or " " not in  Project_descriptions :
            project1.project_description=Project_descriptions 
        
        if len(Project_Url)>=7:
            project1.project_url= Project_Url
            
        if "github.com" in Project_Github_Repo:
            project1.project_github_repo=Project_Github_Repo
        
        project1.save()
        
        messages.info(request, 'Updated!!')

        return redirect('/projects/myprojects')
    
    else:
        project_QUERY=ProjectDetail.objects.get(id=project_id)
        category_QUERYSET=ProjectCategory.objects.values_list('category_name',flat=True).distinct
        label_QUERYSET=ProjectLabel.objects.values_list('label_name',flat=True).distinct
        context={
            "project": project_QUERY,
            "categories": category_QUERYSET,
            "labels": label_QUERYSET
        }
        return render(request,'projects/edit_project_page.html',context)

#--------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def myProjects(request):
    
    projects_QUERYSET=ProjectDetail.objects.filter(user=request.user).order_by('-project_use_count')
    
    context={
        "user_nickname": request.user.nickname,
        "projects": projects_QUERYSET
    }
    
    return render(request,'projects/see_my_projects_page.html',context)


'''
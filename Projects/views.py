from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .utils import request_for_image

from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.

def projectsHome(request):
    category_QUERYSET=[]
    projects_QUERYSET=[]
    
    cats=ProjectCategory.objects.all()
    
    for cat in cats:
        category_QUERYSET.append(cat)
        projects_QUERYSET.append(ProjectDetail.objects.filter(category=cat).order_by('-project_use_count')[0:3])
    
    p_data=zip(category_QUERYSET,projects_QUERYSET)
    
    context={
        'project_data': p_data
    }
    
    return render(request,'projects/project_home_page.html',context)


def allProjects(request,category_id):
    
    
    projects_QUERYSET=ProjectDetail.objects.filter(category=category_id).order_by('-project_use_count')
    category_name=ProjectCategory.objects.get(id=category_id).category_name
    
    context={
        "Project_type": category_name,
        "projects": projects_QUERYSET
    }
    
    return render(request,'projects/see_all_projects_page.html',context)

def ProjectOverview(request,project_id):
    
    
    project_QUERY=ProjectDetail.objects.get(id=project_id)
    
    project_QUERY.project_use_count += 1
    project_QUERY.save()
    
    context={
        "Project_name": project_QUERY.project_name,
        "project": project_QUERY
    }
    return render(request,'projects/project_overview_page.html',context)


def registerProject(request):
    
    if request.method =="POST":
        try:
            data=request.POST
        
            Project_Name=data.get("Project_Name")
            Project_descriptions=data.get("About_Project")
            
            Project_Status=data.get("Status")
            Project_Category=data.get("Category")
            Project_Category=ProjectCategory.objects.get(category_name=Project_Category)
            
            Project_Label=data.get("Label")
            Project_Label=ProjectLabel.objects.get(label_name=Project_Label)
            
            Nickname=request.user.nickname
            
            import random
            
            image_index= random.randint(1,25)
            
            Project_External_Photo=request_for_image(Project_Name, per_page=image_index)[image_index-1]
            
            Project_Url=data.get("Project_Url")
            Project_Github_Repo=data.get("Github_Repository")
            
            new_project=ProjectDetail.objects.create(
                user=request.user,
                category=Project_Category,
                label=Project_Label,
                nickname=Nickname,
                project_name=Project_Name,
                
                project_status=Project_Status,
                project_external_image=Project_External_Photo
            )
            
            if Project_descriptions != "" :
                new_project.project_description=Project_descriptions 
            
            if len(Project_Url)>=7:
                new_project.project_url= Project_Url
                
            if "github.com" in Project_Github_Repo:
                new_project.project_github_repo=Project_Github_Repo
            
            
            new_project.save()
            
            messages.info(request, 'Register!! waiting for varification.')
            
            return redirect('/projects/myprojects')
        
        except EOFError:
            messages.info(request, EOFError)
            
            return redirect('/projects/registerproject')
            
    else:
        category_QUERYSET=ProjectCategory.objects.all()
        label_QUSERSET=ProjectLabel.objects.all()
        context={
            'categories':category_QUERYSET,
            "labels": label_QUSERSET
        }
        return render(request,'projects/register_project_page.html',context)

def updateProject(request,project_id):
    
    proj_id=project_id
    
    if request.method=="POST":
        
        data=request.POST
        
        Project_Name=data.get("Project_Name")
        Project_descriptions=data.get("About_Project")
        
        Project_Status=data.get("Status")
        Project_Category=data.get("Category")
        Project_Label=data.get("Label")
        Category_Object=ProjectCategory.objects.get(category_name=Project_Category)
        Label_Object=ProjectLabel.objects.get(label_name=Project_Label)
        
        Project_Url=data.get("Project_Url")
        Project_Github_Repo=data.get("Github_Repository")
        
        
        project1=ProjectDetail.objects.get(id=proj_id)
        
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


def myProjects(request):
    
    projects_QUERYSET=ProjectDetail.objects.filter(user=request.user).order_by('-project_use_count')
    
    context={
        "user_nickname": request.user.nickname,
        "projects": projects_QUERYSET
    }
    
    return render(request,'projects/see_my_projects_page.html',context)
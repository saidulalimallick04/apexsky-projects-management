from django.shortcuts import render,redirect,resolve_url
from django.contrib import messages

from Projects.models import ProjectCatalog, ProjectLabel, Project
from django.contrib.auth import get_user_model

# Create your views here.

Users=get_user_model()

#--------------------------------------------------------------------------------------------------------------------------------
def home_page(request):
    """
        This Function return the Home Page or Landing Page.\n
        Context Values: [ popularProjects(QUERYSET), upCommingProjects(QUERYSET), projectCatalogs(QUERYSET) ]
    """
    try:
        randomProjects = Project.objects.filter(is_verified = True).order_by("?")[:8]
        upCommingProjects=Project.objects.filter(status='Comming Soon').order_by("?")[:4]
        projectCatalogs = ProjectCatalog.objects.order_by("?")
        
        context={
            "randomProjects" : randomProjects,
            'upCommingProjects': upCommingProjects,
            'projectCatalogs' : projectCatalogs,
        }
        return render(request, "home/index.html",context)
    
    except Exception as e:
        print("Error: ", e)
        return render(request, "home/index.html")

#--------------------------------------------------------------------------------------------------------------------------------
def explore_page(request):
    """
        This Function return Explore Page. This page shows all functionality of our platform.\n
        ContextValues: [  ]
    """
    new_live_projects = Project.objects.filter(status = 'Live').order_by("?")[:8]
    top_5_labels = ProjectLabel.objects.all() [:5] 
    

    context = {
        "new_live_projects" : new_live_projects,
        "top_5_labels" : top_5_labels,

    }

    return render(request=request, template_name="home/explore_page.html",context=context)


#--------------------------------------------------------------------------------------------------------------------------------
def url_not_found(request):
    """
        When the project/event does not have a Deployed/GitHub URL.\n
        Context Values: [  ]
    """
    messages.info(request, 'Url Not Found')
    return redirect(resolve_url("landing-page"))


#--------------------------------------------------------------------------------------------------------------------------------
def search_page(request):
    """
        This is the Search Page.\n
        Context Values: [ Users(QUERYSET), Catalogs(QUERYSET), Projects(QUERYSET) ]
    """
    keyword=request.GET.get('searchKeyword')
    if not keyword:
        return render(request, "home/search_page.html")
    users_QUERYSET=Users.objects.filter(username__icontains = keyword)[0:4]
    category_QUERYSET=ProjectCatalog.objects.filter(name__icontains = keyword)[0:4]
    projects_QUERYSET=Project.objects.filter(name__icontains = keyword)[0:4]
    
    context={
        
        "Users":users_QUERYSET,
        "Catalogs":category_QUERYSET,
        "Projects":projects_QUERYSET,
        "searchKeyword":keyword,
    }
    return render(request, 'home/search_page.html',context)
#--------------------------------------------------------------------------------------------------------------------------------
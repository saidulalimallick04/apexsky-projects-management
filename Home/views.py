from django.shortcuts import render,redirect
from django.contrib import messages
from Projects.models import ProjectCategory,ProjectLabel,ProjectDetail
from .models import HeroSectionImage

from django.contrib.auth import get_user_model
Users=get_user_model()
# Create your views here.

def home_page(request):
    
    try:
        
        popularProjects = ProjectDetail.objects.filter(is_verified = True).order_by("-project_use_count")[:8]
        
        upCommingProjects=ProjectDetail.objects.filter(project_status='Comming Soon').order_by("-id")[:4]
        
        projectCatalogs = ProjectCategory.objects.all()
        
        context={
            "popularProjects" : popularProjects,
            'upCommingProjects': upCommingProjects,
            'projectCatalogs' : projectCatalogs,
        }
        return render(request, "home/index2.html",context)
    
    except Exception as e:
        print("Error: ", e)
        return render(request, "home/index2.html")


def explore_page(request):
    
    return render(request=request, template_name="home/explore_page.html")


def urlNotFound(request):
    
    messages.info(request, 'Url Not Found')
    return redirect("/")



def search_page(request):
    
    if request.method== "GET":
        
        qurey=request.GET.get('query')
        
        Users_QUERYSET=Users.objects.filter(nickname__icontains=qurey)[0:4]
        Category_QUERYSET=ProjectCategory.objects.filter(category_name__icontains=qurey)[0:4]
        Projects_QUERYSET=ProjectDetail.objects.filter(project_name__icontains=qurey)[0:4]
        
        All_index=['Users','Categories','Projects']
        Data=[Users_QUERYSET,Category_QUERYSET,Projects_QUERYSET]
        
        All=zip(All_index,Data)
        
        context={
            "All":All,
            "Users":Users_QUERYSET,
            "Categories":Category_QUERYSET,
            "Projects":Projects_QUERYSET,
            "QUERY":qurey,
        }
        return render(request, 'home/search_page.html',context)
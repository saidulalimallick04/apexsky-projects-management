from django.shortcuts import render,redirect
from django.contrib import messages
from Projects.models import *
from .models import HeroSectionImage
import random

from django.contrib.auth import get_user_model
Users=get_user_model()
# Create your views here.

def homePage(request):
    
    try:
        x=random.randint(1,20)
        Query=HeroSectionImage.objects.get(id=x)
        HeroImage=[Query.image_one,Query.image_two,Query.image_three]
        
        bigProjects=ProjectDetail.objects.filter(category__category_name='Prime Projects').order_by('-project_use_count')[:4]
        miniProjects=ProjectDetail.objects.filter(category__category_name='Mini Project').order_by('-project_use_count')[:4]
        
        upCommingProjects=ProjectDetail.objects.filter(project_status='Comming Soon')[:4]
        
        announcements='''Image/Media Management in server is not live yet!! still use Unsplace(https://unsplash.com/)'''
        
        context={
            'heroImages': HeroImage,
            'bigProjects': bigProjects,
            'miniProjects': miniProjects,
            'topBlog': None ,
            'upCommingProjects': upCommingProjects,
            "Announcements":announcements
        }
        
        
    except:
        
        return render(request, "home/index.html")


def urlNotFound(request):
    
    messages.info(request, 'Url Not Found')
    return redirect("/")



def searchData(request):
    
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
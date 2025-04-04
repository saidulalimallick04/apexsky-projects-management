from django.shortcuts import render

# Create your views here.


def blogHomepage(request):
    
    
    return render(request, 'blogs/blog_home_page.html')
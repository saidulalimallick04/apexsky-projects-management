from django.shortcuts import render

# Create your views here.


def blogHomepage(request):
    
    
    return render(request, 'blogs/blog_home_page.html')

def createBlog(request):
    
    if request.method =="POST":
        print("Creating Post...")
        
    else:
        return render(request,"blog/blog_create_page.html")
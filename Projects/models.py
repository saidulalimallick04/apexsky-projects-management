from django.db import models

from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.


def setDefaultCategory():
    return ProjectCategory.objects.get_or_create(name="undefined")[0]

def setDefaultLabel():
    return ProjectLabel.objects.get_or_create(name="undefined")[0]

class ProjectCategory(models.Model):
    
    category_name=models.CharField(max_length=50,unique=True)
    category_descriptions=models.TextField(max_length=100,default="--No descriptions--")
    
    class Meta:
        ordering=['category_name']
        verbose_name="Project Category"
        verbose_name_plural="Project Categories"
        
    def __str__(self) -> str:
        return self.category_name
    

class ProjectLabel(models.Model):
    label_name=models.CharField(max_length=50)
    label_descriptions=models.TextField(max_length=200,default="--No descriptions--")
    
    def __str__(self)->str:
        return self.label_name
    

class ProjectDetail(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(ProjectCategory,on_delete=models.SET_DEFAULT,default=setDefaultCategory)
    label=models.ForeignKey(ProjectLabel,models.SET_DEFAULT,default=setDefaultLabel)
    nickname=models.CharField(max_length=15,null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    
    project_image=models.ImageField(upload_to=None,null=True,blank=True)
    project_external_image=models.TextField(max_length=400,null=True,blank=True)
    
    project_name=models.CharField(max_length=50)
    project_description=models.TextField(max_length=150)
    
    project_use_count=models.IntegerField(default=0)
    creation_date=models.DateField(auto_now_add=True)
    Last_update=models.DateField(auto_now=True)
    
    project_status=models.CharField(default='Comming Soon')
    
    project_document_file=models.FileField(upload_to=None,null=True,blank=True)
    project_url=models.URLField(default='/url-not-found',max_length=200,blank=True,null=True)
    project_github_repo=models.URLField(default='/url-not-found',max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.project_name
    
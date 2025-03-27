from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Blog(models.Model):

    user=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default="Unknown User")
    user_nickname=models.CharField(max_length=50,null=True,blank=True)
    blog_title=models.CharField(max_length=50)
    blog_descriptions=models.TextField(max_length=250,default="No Descriptions")
    
    blog_image=models.ImageField(null=True,blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    blog_external_image=models.TextField(max_length=400)
    
    blog_like=models.IntegerField(default=0)
    blog_dislike=models.IntegerField(default=0)
    blog_comments=ArrayField(models.TextField(max_length=100),null=True,blank=True,default=list)
    

    class Meta:
        verbose_name ="Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.blog_title

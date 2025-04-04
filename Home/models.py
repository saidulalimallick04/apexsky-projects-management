from django.db import models

# Create your models here.

class HeroSectionImage(models.Model):

    name=models.CharField(max_length=50)
    image_one=models.TextField(max_length=400)
    image_two=models.TextField(max_length=400)
    image_three=models.TextField(max_length=400)

    def __str__(self):
        return self.name
    
    
class UserFeedBack(models.Model):
    
    name=models,models.CharField(max_length=50)
    
    email=models.EmailField(max_length=254)
    
    time=models.TimeField(auto_now=False, auto_now_add=True)
    
    feedback=models.TextField(max_length=300)
    
    status=models.CharField(max_length=50,default="Pending")
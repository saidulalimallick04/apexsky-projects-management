from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import UserManager


class CustomUser(AbstractUser):
    
    unique_identifier=models.UUIDField( unique=True ,default=uuid.uuid4, editable=False)
    phone_number=models.CharField(max_length=20,blank=True)
    email=models.EmailField(unique=True)
    is_verified=models.BooleanField(default=False)
    username=None

    nickname=models.CharField(max_length=20,blank=True,null=True)
    about_me=models.TextField(max_length=20,blank=True,null=True)
    location=models.TextField(max_length=20,blank=True,null=True)
    profile_pic=models.ImageField(upload_to=None,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    gender=models.TextField(max_length=50,null=True,blank=True)
    
    user_ott=models.TextField(max_length=7,null=True,blank=True)
    USERNAME_FIELD=('email')
    REQUIRED_FIELDS=[]
    
    objects=UserManager()
    
    def __str__(self) -> str:
        return self.email
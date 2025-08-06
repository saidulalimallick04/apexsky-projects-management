from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

import uuid
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    
    profile_image = CloudinaryField(("Profile Image"),
                    resource_type = "image",
                    folder = "apexsky-project-management/avater/",
                    null = True,
                    blank = True)
    unique_identifier=models.UUIDField(unique=True,
                    default=uuid.uuid4,
                    editable=False)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=20,
                    blank=True)
    username=models.CharField(unique=True,
                    max_length=20,
                    blank=True)
    about_me=models.TextField(max_length=100,
                    blank=True)
    location=models.TextField(max_length=25,
                    blank=True)
    date_of_birth=models.DateField(blank=True,null=True)
    gender=models.CharField(max_length=10,
                    blank=True)
    is_verified=models.BooleanField(default=False)
    
    USERNAME_FIELD=('email')
    REQUIRED_FIELDS=["username"]
    
    objects=UserManager()
    
    def __str__(self) -> str:
        return f"{self.username}||>>{self.email}"
    
    # def save(self, *args, **kwargs):
    #     if not self.password.startswith("pbkdf2_sha256$1000000$"):
    #         self.set_password(self.password)
    #     super().save(*args, **kwargs)
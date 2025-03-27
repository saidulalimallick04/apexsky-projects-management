from django.db import models

# Create your models here.

class HeroSectionImage(models.Model):

    name=models.CharField(max_length=50)
    image_one=models.TextField(max_length=400)
    image_two=models.TextField(max_length=400)
    image_three=models.TextField(max_length=400)

    def __str__(self):
        return self.name
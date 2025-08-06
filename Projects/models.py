from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

#------------------------------------------------------------------------------------------------------
class ProjectCatalog(models.Model):
    '''
    It store Project Calalogs/Catagories like App Development, Frontend Development etc.
    '''
    thumbnail_image = CloudinaryField(
                        resource_type = "image",
                        folder = "apexsky-project-management/project-catagory-images/",
                        null = True,
                        blank = True)    
    name=models.CharField(
                        max_length=50,
                        unique=True)
    handle = models.CharField(
                        max_length= 75,
                        null= True,
                        unique= True,
                        editable= False)
    descriptions=models.TextField(
                        max_length=100,
                        blank=True)
    
    class Meta:
        ordering=['name']
        verbose_name="Project Catalog"
        verbose_name_plural="Project Catalogs"
        
    def __str__(self) -> str:
        """
            This Function will help when we call the Object. This will help to easily identify Records/Rows.
        """
        return f"{self.name}"
    
    def set_handle(self):
        self.handle = f"@{self.name.lower().replace(" ","_")}"

    def save(self, *args, **kwargs):
        self.set_handle()
        super().save(*args, **kwargs)
    
#------------------------------------------------------------------------------------------------------
class ProjectLabel(models.Model):
    '''
    This Store the label of project like Hobbie Project, Hackathon Project, Final Year Project etc. 
    '''
    thumbnail_image = CloudinaryField(
                        resource_type = "image",
                        folder = "apexsky-project-management/project-label-images/",
                        null = True,
                        blank = True)
    name = models.CharField(
                        max_length= 50,
                        unique= True)
    handle = models.CharField(
                        max_length = 75,
                        null = True,
                        unique = True,
                        editable = False)
    descriptions = models.TextField(
                        max_length = 100,
                        blank = True)
    
    class Meta:
        ordering=['name']
        verbose_name="Project Label"
        verbose_name_plural="Project Labels"
    
    def __str__(self) -> str:
        """
            This Function will help when we call the Object. This will help to easily identify Records/Rows.
        """
        return f"{self.name}"
    
    def set_handle(self):
        self.handle = f"@{self.name.lower().replace(" ","_")}"

    def save(self, *args, **kwargs):
        self.set_handle()
        super().save(*args, **kwargs)
    
#------------------------------------------------------------------------------------------------------

class Project(models.Model):
    '''
    This Store project data.
    '''
    user = models.ForeignKey(User,
                        related_name= "User",
                        on_delete = models.CASCADE,
                        default = None)
    category = models.ForeignKey(ProjectCatalog,
                        related_name = "ProjectCatalog",
                        on_delete = models.SET_DEFAULT,
                        default = None)
    label = models.ForeignKey(ProjectLabel,
                        related_name = "ProjectLabel",
                        on_delete = models.SET_DEFAULT,
                        default = None)
    
    thumbnail_image = CloudinaryField(
                        resource_type = "image",
                        folder = "apexsky-project-management/project-images/",
                        null = True,
                        blank = True) 
    name = models.CharField(
                        max_length = 50)
    handle = models.CharField(
                        max_length = 50,
                        null = True,
                        unique = True,
                        editable = False)
    content = models.TextField(
                        max_length = 500,
                        blank = True)
    user_username = models.CharField(
                        max_length = 30)
    use_count = models.IntegerField(   
                        default = 0)
    creation_date = models.DateField(
                        auto_now_add = True)
    Last_update = models.DateField(
                        auto_now = True)
    status = models.CharField(
                        default = 'Comming Soon')
    is_verified = models.BooleanField(verbose_name=("Verification Status(True/False)"),
                        default = False)
    
    framework = models.CharField(
                        max_length = 25,
                        blank = True)
    document_file = CloudinaryField(
                        resource_type = "raw",
                        folder = "apexsky-project-management/project-documents/",
                        null = True,
                        blank = True) 
    deployed_url = models.URLField(
                        max_length = 300,
                        blank = True)
    github_repository = models.URLField(
                        max_length = 300,
                        blank = True)
    demo_video = models.URLField(
                        max_length = 300,
                        blank = True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        """
            This Function will help when we call the Object. This will help to easily identify Records/Rows.
        """
        return f"{self.name} (Developed_By {self.user_username})"
    
    def set_handle(self):
        """
            This Function will help to set Project.handle\n
            Structure: [ f"{self.name}"]
        """
        base_handle = f"@{self.name.lower().replace(' ', '_')}"
        handle = base_handle
        base_name = self.name
        new_name = base_name
        counter = 0
        
        while Project.objects.filter(handle=handle).exclude(id=self.id).exists():
            counter += 1
            handle = f"{base_handle}_{counter}"
            new_name = f"{base_name} {counter}"

        self.name = new_name
        self.handle = handle

    def save(self, *args, **kwargs):
        self.set_handle()
        super().save(*args, **kwargs)
#------------------------------------------------------------------------------------------------------
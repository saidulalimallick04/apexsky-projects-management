from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

import uuid
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    
    """
    -----------------Pre-Defined in AbstractUser Class----------------------------

        username_validator = UnicodeUsernameValidator()

        username = models.CharField(
            _("username"),
            max_length=150,
            unique=True,
            help_text=_(
                "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
            ),
            validators=[username_validator],
            error_messages={
                "unique": _("A user with that username already exists."),
            },
        )
        first_name = models.CharField(_("first name"), max_length=150, blank=True)
        last_name = models.CharField(_("last name"), max_length=150, blank=True)
        email = models.EmailField(_("email address"), blank=True)
        is_staff = models.BooleanField(
            _("staff status"),
            default=False,
            help_text=_("Designates whether the user can log into this admin site."),
        )
        is_active = models.BooleanField(
            _("active"),
            default=True,
            help_text=_(
                "Designates whether this user should be treated as active. "
                "Unselect this instead of deleting accounts."
            ),
        )
        date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

        objects = UserManager()

        EMAIL_FIELD = "email"
    """
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
    

    liked_project = models.ManyToManyField("Projects.Project",
                    verbose_name=("Liked Project"),
                    through="Projects.ProjectLike")
    USERNAME_FIELD=('email')
    REQUIRED_FIELDS=["username"]
    
    objects=UserManager()
    
    def __str__(self) -> str:
        return f"{self.username} (Email:{self.email})"
    
    # def save(self, *args, **kwargs):
    #     if not self.password.startswith("pbkdf2_sha256$1000000$"):
    #         self.set_password(self.password)
    #     super().save(*args, **kwargs)

    #-------------------------------------------------------------------------------------------------------------


class OtpData(models.Model):
    email = models.EmailField(("Email"),
                        primary_key=True,
                        unique=True,
                        max_length=254)
    otp = models.CharField(("One Time Password"),
                        max_length=10,
                        null=True,
                        blank=True)
    
    created_date= models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.email} ||| {self.otp}'
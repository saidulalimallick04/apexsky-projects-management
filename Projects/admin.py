from django.contrib import admin
from .models import ProjectCatalog, ProjectLabel, Project, ProjectLike

# Register your models here.

admin.site.register(ProjectCatalog)
admin.site.register(ProjectLabel)
admin.site.register(Project)
admin.site.register(ProjectLike)
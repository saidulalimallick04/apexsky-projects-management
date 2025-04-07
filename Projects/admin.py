from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(ProjectCategory)
admin.site.register(ProjectDetail)
admin.site.register(ProjectLabel)
from atexit import register
from django.contrib import admin
from .models import Project, ProjectImage, ProjectVideo

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(ProjectVideo)
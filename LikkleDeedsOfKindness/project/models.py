from email.mime import image
from django.db import models
from cause.models import Cause

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    caption = models.CharField(max_length=225)

class ProjectVideos(models.Model):
    video_link = models.CharField(max_length=225)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

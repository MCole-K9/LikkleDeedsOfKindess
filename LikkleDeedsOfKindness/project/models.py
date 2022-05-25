from email.mime import image
from django.db import models
from cause.models import Cause

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    video_link = models.CharField(max_length=225, default="none")

    def __str__(self):
        return self.title
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    caption = models.CharField(max_length=225)

class ProjectVideo(models.Model):
    video_link = models.CharField(max_length=225)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

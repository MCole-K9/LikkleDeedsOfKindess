
from sysconfig import parse_config_h
from django.db import models

# Create your models here.

class Cause(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

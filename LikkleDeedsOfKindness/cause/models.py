from django.db import models
import datetime

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
    parish = models.CharField(max_length=200, default="None")
    date = models.DateTimeField(default=datetime.datetime.now)#time zone support is enable, factor in
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

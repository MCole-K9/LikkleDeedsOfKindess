from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=60)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=225)

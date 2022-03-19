from django.db import models
from cause.models import Cause

# Create your models here.
class Donor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=60)
    phone_number = models.CharField(max_length=20)


class Donation(models.Model):
    amount = models.FloatField()
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)



from django.db import models
from cause.models import Event

# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=60)
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.first_name } {self.last_name}" 


class GeneralVolunteer(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

class AdminVolunteer(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

class EventVolunteer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
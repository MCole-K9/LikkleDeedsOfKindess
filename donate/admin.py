from django.contrib import admin
from .models import Donation, Donor

# Register your models here.
admin.site.register(Donor)
admin.site.register(Donation)
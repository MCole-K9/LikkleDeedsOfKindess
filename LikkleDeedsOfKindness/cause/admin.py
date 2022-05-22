from django.contrib import admin
from .models import Cause, Event

# Register your models here.
admin.site.register(Cause)
admin.site.register(Event)
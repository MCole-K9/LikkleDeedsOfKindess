from django.contrib import admin
from .models import Cause, Event, CauseCategory

# Register your models here.
admin.site.register(Cause)
admin.site.register(Event)
admin.site.register(CauseCategory)

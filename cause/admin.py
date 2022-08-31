from django.contrib import admin
from .models import Cause, Event, CauseCategory, SuccessStory

# Register your models here.
admin.site.register(Cause)
admin.site.register(Event)
admin.site.register(CauseCategory)
admin.site.register(SuccessStory)

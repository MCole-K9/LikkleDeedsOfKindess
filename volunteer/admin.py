import imp
from django.contrib import admin
from .models import Volunteer, AdminVolunteer, GeneralVolunteer, EventVolunteer

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(AdminVolunteer)
admin.site.register(GeneralVolunteer)
admin.site.register(EventVolunteer)
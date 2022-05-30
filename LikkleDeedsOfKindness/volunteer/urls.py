from django.urls import path
from . import views

app_name = "volunteer"

urlpatterns = [
    path("", views.volunteer, name="Volunteer"),
    path("EventVolunteer/<int:event_id>", views.event_volunteer, name="EventVolunteer"),
    path("AdminVolunteer", views.admin_volunteer, name="AdminVolunteer"),
    path("GeneralVolunteer", views.general_volunteer, name="GeneralVolunteer"),
]

from django.urls import path
from . import views

app_name = "volunteer"

urlpatterns = [
    path("", views.volunteer, name="Volunteer"),
    #path("/Form", views.volunteer_form, name="Volunteer Form")
]

from django.urls import path
from . import views

app_name = "donate"
urlpatterns = [
    path("", views.donate, name="Donate"),
    path("Cause/<int:id>", views.donate_cause, name="DonateCause")

]

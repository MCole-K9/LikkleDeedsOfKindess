
from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("<int:id>", views.project, name="Project")
]
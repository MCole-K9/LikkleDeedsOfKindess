from sys import path_hooks
from django.urls import  path, re_path
from . import views

app_name = "user"

urlpatterns = [
    path("Dashboard", views.dashboard, name="Dashboard"),
    path("Volunteers", views.volunteers, name="Volunteers"),
    path("ManageCauses", views.manage_causes, name="ManageCauses"),
    path("AddCause", views.add_cause, name="AddCause"),
    path("EditCause/<int:id>", views.edit_cause, name="EditCause")

]
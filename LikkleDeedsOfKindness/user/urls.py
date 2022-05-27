from sys import path_hooks
from django.urls import  path, re_path
from . import views

app_name = "user"

urlpatterns = [
    path("Dashboard", views.dashboard, name="Dashboard"),
    path("Volunteers", views.volunteers, name="Volunteers"),
    path("ManageCauses", views.manage_causes, name="ManageCauses"),
    path("AddCause", views.add_cause, name="AddCause"),
    path("EditCause/<int:id>", views.edit_cause, name="EditCause"),
    path("DeleteCause/<int:id>", views.delete_cause, name="DeleteCause"),
    path("CauseProjects/<int:id>", views.cause_projects, name="CauseProjects"),
    path("AddProject/<int:cause_id>", views.add_project, name="AddProject"),
    path("EditProject/<int:id>", views.edit_project, name="EditProject"),
    path("DeleteProject/<int:id>", views.delete_project, name="DeleteProject"),
    path("ProjectImages/<int:id>", views.project_images, name="ProjectImages"),
    path("AddImage/<int:project_id>", views.add_image, name="AddImage"),
    path("EditImage/<int:id>", views.edit_image, name="EditImage"),
    path("DeleteImage/<int:id>", views.delete_image, name="DeleteImage"),


]
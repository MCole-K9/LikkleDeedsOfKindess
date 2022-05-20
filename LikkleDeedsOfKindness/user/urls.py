from django.urls import URLPattern, path
from . import views

app_name = "user"

urlpatterns = [
    path("Dashboard", views.dashboard, name="Dashboard"),
    path("Volunteers", views.volunteers, name="Volunteers")
]
from django.urls import URLPattern, path
from . import views

name = "user"

urlpatterns = [
    path("Dashboard", views.dashboard, name="Dashboard")
]
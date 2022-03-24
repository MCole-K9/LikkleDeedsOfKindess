from django.urls import  path
from . import views

app_name = "cause"
urlpatterns = [
    path("", views.cause, name="Cause"),
    path("Events", views.events, name="Events"),
    path("Detail", views.cause_detail, name="Detail")
]
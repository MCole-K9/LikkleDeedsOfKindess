from django.urls import  path
from . import views

app_name = "cause"
urlpatterns = [
    path("", views.cause, name="Cause"),
    path("Events", views.events, name="Events"),
    path("Event/<int:id>/Detail", views.event_detail, name="EventDetail"),
    path("Detail/<int:id>", views.cause_detail, name="Detail")
]
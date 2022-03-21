from django.urls import  path
from . import views

app_name = "cause"
urlpatterns = [
    path("", views.cause, name="Cause"),
    
]
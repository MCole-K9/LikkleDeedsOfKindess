from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse
from cause.models import Cause, Event, SuccessStory
from project.models import ProjectImage
from django.contrib.auth import authenticate, login, logout
import datetime, time



def index(request):

    now = datetime.datetime.now()
    str_now = now.strftime("%Y-%m-%d %H:%M")
    
     
    causes = Cause.objects.all()[:4]
    events = Event.objects.filter(date__gte=str_now)[:3]

    project_images = ProjectImage.objects.all()[:6:-1]

    stories = SuccessStory.objects.all()

    context = {
        "causes": causes,
        "images": project_images,
        "events" : events,
        "stories": stories
    }

    return render(request, "index.html", context)   

def about(request):
    return render(request, "about.html", {})

def gallery(request):
    project_images = ProjectImage.objects.all()[::-1]
    context = {
        "images" : project_images
    }
    return render(request, "gallery.html", context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:

            login(request, user)
            return redirect(reverse("user:Dashboard"))

    return render(request, "login.html", {})


def logout_user(request):

    logout(request)
    return redirect("/")


def view_story(request, id):

    story = get_object_or_404(SuccessStory, pk=id)

    context = {
        "story": story
    }

    return render(request, "successstory.html", context)
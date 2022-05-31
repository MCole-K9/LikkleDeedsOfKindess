from django.shortcuts import render
from django.http import HttpResponse
from cause.models import Cause, Event
from project.models import ProjectImage
import datetime, time



def index(request):

    now = datetime.datetime.now()
    str_now = now.strftime("%Y-%m-%d %H:%M")
    
     
    causes = Cause.objects.all()[:4]
    events = Event.objects.filter(date__gte=str_now)[:3]

    
    

    project_images = ProjectImage.objects.all()[:6:-1]
    context = {
        "causes": causes,
        "images": project_images,
        "events" : events
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
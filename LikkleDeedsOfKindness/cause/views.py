from django.shortcuts import get_object_or_404, render
from .models import Cause, Event, CauseCategory
from project.models import Project
import datetime

# Create your views here.

def cause(request):

    causes = Cause.objects.all()
    categories = CauseCategory.objects.all()
    context = {
        "causes": causes,
        "categories": categories,
    }

    return render(request, "cause.html", context)

def cause_category(request, id):

    # category = get_object_or_404(CauseCategory, pk=id)

    causes = Cause.objects.filter(category=id)
    
    categories = CauseCategory.objects.all()
    context = {
        "causes": causes,
        "categories": categories,
    }
    return render(request, "cause.html", context)

def events(request):

    now = datetime.datetime.now()
    str_now = now.strftime("%Y-%m-%d %H:%M")
    events = Event.objects.filter(date__gte=str_now)

    return render(request, "events.html", {"events": events}) 

def event_detail(request, id):
    
    event = get_object_or_404(Event, pk=id)
    context = {
        "event": event
    }
    return render(request, "eventdetail.html", context)

def cause_detail(request, id):

    cause = Cause.objects.get(pk=id)
    projects = Project.objects.filter(cause=id)
    
    context = {
        "cause": cause,
        "projects": projects
    }

    return render(request, "causedetail.html", context)

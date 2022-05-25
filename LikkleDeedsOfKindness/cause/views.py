from django.shortcuts import render
from .models import Cause
from project.models import Project

# Create your views here.

def cause(request):

    causes = Cause.objects.all()
    context = {
        "causes": causes,
    }

    return render(request, "cause.html", context)

def events(request):
    return render(request, "events.html", {}) 

def cause_detail(request, id):

    cause = Cause.objects.get(pk=id)
    projects = Project.objects.filter(cause=id)
    
    context = {
        "cause": cause,
        "projects": projects
    }

    return render(request, "causedetail.html", context)

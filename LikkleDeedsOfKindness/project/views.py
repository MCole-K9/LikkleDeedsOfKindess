from django.shortcuts import render
from .models import Project

# Create your views here.
def project(request, id):

    project:Project = Project.objects.get(pk=id)

    context = {

        "project": project
    }
    return render(request, "project.html", context)
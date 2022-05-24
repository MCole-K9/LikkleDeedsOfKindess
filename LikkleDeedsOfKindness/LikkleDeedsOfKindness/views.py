from django.shortcuts import render
from django.http import HttpResponse
from cause.models import Cause, Event




def index(request):

    causes = Cause.objects.all()
    context = {
        "causes": causes,
    }

    return render(request, "index.html", {})   

def about(request):
    return render(request, "about.html", {})

def gallery(request):
    return render(request, "gallery.html", {})
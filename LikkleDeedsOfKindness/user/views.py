
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from cause.models import Cause

# Create your views here.

def dashboard(request):
    return render(request, "Dashboard.html", {})

def volunteers(request):
    return render(request, "Volunteers.html", {})

def manage_causes(request):

    causes = Cause.objects.all()
    context = {
        "causes": causes,
    }

    return render(request, "ManageCauses.html", context)

def add_cause(request):

    if request.method == "POST":
        
        cause = Cause()
        cause.title = request.POST["title"]
        cause.description = request.POST["description"]
        cause.content = request.POST["body"]
        cause.image = request.FILES["display_image"]
        cause.save()

        return HttpResponseRedirect(reverse("user:ManageCauses")) 
        
    return render(request, "AddCause.html", {})

def edit_cause(request, id):

    cause:Cause = Cause.objects.get(pk=id)

    if request.method == "POST":

        cause.title = request.POST["title"]
        cause.description = request.POST["description"]
        cause.content = request.POST["body"]

        if(request.FILES):
            cause.image = request.FILES["display_image"]

        cause.save()

        return HttpResponseRedirect(reverse("user:ManageCauses"))
        
    else:

        context = {
            "cause": cause,
        }
        return render(request, "AddCause.html", context)


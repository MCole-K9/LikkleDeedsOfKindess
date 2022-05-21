
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def dashboard(request):
    return render(request, "Dashboard.html", {})

def volunteers(request):
    return render(request, "Volunteers.html", {})

def manage_causes(request):
    return render(request, "ManageCauses.html", {})

def add_cause(request):

    if request.method == "POST":
        #print(request.POST["title"])
        return HttpResponseRedirect(reverse("user:ManageCauses")) 
        
    return render(request, "AddCause.html", {})
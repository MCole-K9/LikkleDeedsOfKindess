from django.shortcuts import render

# Create your views here.

def cause(request):
    return render(request, "cause.html", {})

def events(request):
    return render(request, "events.html", {}) 

def cause_detail(request):
    return render(request, "causedetail.html", {})

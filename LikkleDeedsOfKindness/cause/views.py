from django.shortcuts import render

# Create your views here.

def cause(request):
    return render(request, "cause.html", {})   
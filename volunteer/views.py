from django.shortcuts import get_object_or_404, redirect, render
from .models import EventVolunteer, Volunteer, AdminVolunteer, GeneralVolunteer
from cause.models import Event

# Create your views here.
def volunteer(request):
    return render(request, "volunteer.html", {})

def event_volunteer(request, event_id):

    event:Event = get_object_or_404(Event, pk=event_id)

    #ensures that data isn't duplicated
    volunteer , created = Volunteer.objects.get_or_create(
        email=request.POST["email"].lower(),
        defaults={
            "first_name" : request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "phone_number": request.POST["phone_number"] ,
        }
    )

    if not created:
        volunteer.first_name = request.POST["first_name"]
        volunteer.last_name = request.POST["last_name"]
        volunteer.phone_number = request.POST["phone_number"],
        volunteer.save()


    EventVolunteer.objects.get_or_create(event=event, volunteer=volunteer)

    


    return redirect("/")

def admin_volunteer(request):

    if request.method == "POST":
        volunteer , created = Volunteer.objects.get_or_create(
        email=request.POST["email"].lower(),
        defaults={
            "first_name" : request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "phone_number": request.POST["phone_number"] ,
            }
        )

        if not created:
            volunteer.first_name = request.POST["first_name"]
            volunteer.last_name = request.POST["last_name"]
            volunteer.phone_number = request.POST["phone_number"],
            volunteer.save()

        
        AdminVolunteer.objects.get_or_create(volunteer=volunteer)

    return redirect("/")

def general_volunteer(request):

    if request.method == "POST":
        volunteer , created = Volunteer.objects.get_or_create(
        email=request.POST["email"].lower(),
        defaults={
            "first_name" : request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "phone_number": request.POST["phone_number"] ,
            }
        )

        if not created:
            volunteer.first_name = request.POST["first_name"]
            volunteer.last_name = request.POST["last_name"]
            volunteer.phone_number = request.POST["phone_number"],
            volunteer.save()

        
        GeneralVolunteer.objects.get_or_create(volunteer=volunteer)

    return redirect("/")

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Donation, Donor
from cause.models import Cause
from django.contrib import messages
import json


# Create your views here.


def donate(request):
    
    if request.method == "POST":
        #sent over data using the fetch api
        data = json.loads(request.body.decode("utf-8"))

        #use get or create
        donor , created = Donor.objects.get_or_create(email=data["email"], defaults={
            "first_name": data["firstName"],
            "last_name":  data["lastName"],
            "phone_number": data["phoneNumber"]
        })

        if not created:

            donor.first_name = data["firstName"]
            donor.last_name = data["lastName"]
            donor.phone_number = data["phoneNumber"]

            donor.save()

        donation:Donation = Donation()

        donation.donor = donor
        donation.amount = data["amount"]

        #value in hidden input on donate template
        cause_id = int(data["cause"])

        if cause_id > 0:
            cause = get_object_or_404(Cause, pk=cause_id)
            donation.cause = cause

        donation.save()

        messages.add_message(request, messages.SUCCESS, f"{donor}, Thank You For Your Donation!")

        response_data = {
            "status": 200,
            "message": "success"
        }

        return JsonResponse(response_data)

    return render(request, "donate.html", {})

def donate_cause(request, id):

    cause = get_object_or_404(Cause, pk=id)

    return render(request, "donate.html", {"cause":cause})
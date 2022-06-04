from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Donation, Donor
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

        donation.save()

        messages.add_message(request, messages.SUCCESS, f"{donor}, Thank You For Your Donation!")

        response_data = {
            "status": 200,
            "message": "success"
        }

        return JsonResponse(response_data)

    return render(request, "donate.html", {})
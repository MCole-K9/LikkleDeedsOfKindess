import datetime
from time import strftime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from cause.models import Cause, Event, CauseCategory, SuccessStory
from project.models import Project, ProjectImage
from volunteer.models import EventVolunteer, AdminVolunteer, GeneralVolunteer
from donate.models import Donation, Donor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/Login")
def dashboard(request):

    month = datetime.datetime.now().month

    donations = Donation.objects.all().order_by("date")[::-1]
    m_donations = Donation.objects.filter(date__month=month)

    donation_sum = 0 
    m_donation_sum = 0


    for donation in donations:
        donation_sum += donation.amount

    for donation in m_donations:
        m_donation_sum += donation.amount

    context = {
        "donations": donations,
        "total_donors": Donor.objects.count(),
        "donation_sum": donation_sum,
        "m_donation_sum": m_donation_sum,

    }
    return render(request, "Dashboard.html", context)


@login_required(login_url="/Login")
def volunteers(request):
    now = datetime.datetime.now()
    str_now = now.strftime("%Y-%m-%d %H:%M")
    
    event_volunteers = EventVolunteer.objects.filter(event__date__gte=str_now)

    admin_volunteers = AdminVolunteer.objects.all()
    general_volunteers = GeneralVolunteer.objects.all()

    context = {
        "event_volunteers":  event_volunteers,
        "admin_volunteers": admin_volunteers,
        "general_volunteers": general_volunteers
    }
    return render(request, "Volunteers.html", context)


@login_required(login_url="/Login")
def manage_causes(request):

    causes = Cause.objects.all()
    context = {
        "causes": causes,
    }

    return render(request, "ManageCauses.html", context)


@login_required(login_url="/Login")
def add_cause(request):
    categories = CauseCategory.objects.all()

    if request.method == "POST":

        category = get_object_or_404(CauseCategory, pk=request.POST["category"])
        
        cause = Cause()
        cause.title = request.POST["title"]
        cause.description = request.POST["description"]
        cause.content = request.POST["body"]
        cause.category = category

        if request.FILES:
            cause.image = request.FILES["display_image"]

        cause.save()

        return HttpResponseRedirect(reverse("user:ManageCauses")) 
        
    return render(request, "AddCause.html", {"categories": categories})


@login_required(login_url="/Login")
def edit_cause(request, id):

    cause:Cause = Cause.objects.get(pk=id)
    categories = CauseCategory.objects.all()

    if request.method == "POST":

        category = get_object_or_404(CauseCategory, pk=request.POST["category"])

        cause.title = request.POST["title"]
        cause.description = request.POST["description"]
        cause.content = request.POST["body"]
        cause.category = category

        if(request.FILES):
            cause.image = request.FILES["display_image"]

        cause.save()
        

        return HttpResponseRedirect(reverse("user:ManageCauses"))
        
    else:

        context = {
            "cause": cause,
            "categories": categories,

        }
        return render(request, "AddCause.html", context)

@login_required(login_url="/Login")
def delete_cause(request, id):

    cause:Cause = Cause.objects.get(pk=id)
    cause.delete()

    return redirect(reverse("user:ManageCauses"))


@login_required(login_url="/Login")
def cause_projects(request, id):
    
    projects =  Project.objects.filter(cause=id) 

    context = {
        "projects" : projects,
        "cause": id,
        
    }

    return render(request, "CauseProjects.html", context)


@login_required(login_url="/Login")
def add_project(request, cause_id):

    if request.method == "POST":

        project:Project = Project()

        cause:Cause = Cause.objects.get(pk=cause_id)
        PostData =  request.POST

        project.cause = cause
        project.title = PostData["title"]
        project.description = PostData["description"]
        project.video_link = PostData["video_link"]
        project.content = PostData["body"]          

        project.save()

       

        images = request.FILES.getlist("project_images")
        if request.FILES:
            for index, image in enumerate(images):
                project_image:ProjectImage = ProjectImage()
                project_image.project = project
                project_image.image = image
                project_image.caption  = PostData[f"caption{index}"]
                project_image.save()

        return redirect(reverse("user:CauseProjects", args=[cause_id]))

    return render(request, "AddProject.html", {"cause_id": cause_id})


@login_required(login_url="/Login")
def edit_project(request, id):

    project:Project = Project.objects.get(pk=id)

    if request.method == "POST":

        PostData =  request.POST

        project.title = PostData["title"]
        project.description = PostData["description"]
        project.video_link = PostData["video_link"]
        project.content = PostData["body"]          

        project.save()

        images = request.FILES.getlist("project_images")
        if request.FILES:
            for index, image in enumerate(images):
                project_image:ProjectImage = ProjectImage()
                project_image.project = project
                project_image.image = image
                project_image.caption  = PostData[f"caption{index}"]
                project_image.save()

        return redirect(reverse("user:CauseProjects", args=[project.cause.pk]))

    return render(request, "AddProject.html", {"project": project})


@login_required(login_url="/Login")
def delete_project(request, id):

    project:Project = Project.objects.get(pk=id)

    cause_id = project.cause.pk

    project.delete()

    return redirect(reverse("user:CauseProjects", args=[cause_id]))


@login_required(login_url="/Login")
def project_images(request, id):

    images = ProjectImage.objects.filter(project=id)
    
    context = {
        "images": images
    }
    return render(request, "ProjectImages.html", context)


@login_required(login_url="/Login")
def add_image(request, project_id):

    project = Project.objects.get(pk=project_id)

    if request.method == "POST":

        project_image:ProjectImage = ProjectImage()
        
        project_image.project = project

        project_image.caption = request.POST["caption"]

        if request.FILES:
            project_image.image = request.FILES["image"]
        
        project_image.save()

    return redirect(reverse("user:ProjectImages", args=[project_id]))


@login_required(login_url="/Login")
def edit_image(request, id):

    if request.method == "POST":
        project_image:ProjectImage = ProjectImage.objects.get(pk=id)

        project_image.caption = request.POST["caption"]

        if request.FILES:
            project_image.image = request.FILES["image"]
        
        project_image.save()

    return redirect(reverse("user:ProjectImages", args=[project_image.project.pk]))
    


@login_required(login_url="/Login")
def delete_image(request, id):

    project_image:ProjectImage = ProjectImage.objects.get(pk=id)

    project_id = project_image.project.pk

    project_image.delete()

    return redirect(reverse("user:ProjectImages", args=[project_id]))



@login_required(login_url="/Login")
def manage_events(request):

    events = Event.objects.all()
    context = {
        "events": events
    }
    return render(request, "ManageEvents.html", context)


@login_required(login_url="/Login")
def add_event(request):

    if request.method == "POST":
        event:Event = Event()
        event.title = request.POST["title"]
        event.description = request.POST["description"]
        event.city = request.POST["city"]
        event.street = request.POST["street_address"]
        event.parish = request.POST["parish"]

        post_date:str = request.POST["date"]
        date_parts = post_date.split("-")
        date_parts = [int(element) for element in date_parts]

        post_time:str = request.POST["time"]
        time_parts = post_time.split(":")
        time_parts = [int(element) for element in time_parts]

        

        event.date = datetime.datetime(date_parts[0], date_parts[1], date_parts[2], time_parts[0], time_parts[1])
        event.save()

        #cause from event model is null
        
        return redirect(reverse("user:ManageEvents"))

    return render(request, "AddEvent.html", {})


@login_required(login_url="/Login")
def edit_event(request, id):

    event:Event = get_object_or_404(Event, pk=id)

    if request.method == "POST":
        
        event.title = request.POST["title"]
        event.description = request.POST["description"]
        event.city = request.POST["city"]
        event.street = request.POST["street_address"]
        event.parish = request.POST["parish"]

        post_date:str = request.POST["date"]
        date_parts = post_date.split("-")
        date_parts = [int(element) for element in date_parts]

        post_time:str = request.POST["time"]
        time_parts = post_time.split(":")
        time_parts = [int(element) for element in time_parts]

        

        event.date = datetime.datetime(date_parts[0], date_parts[1], date_parts[2], time_parts[0], time_parts[1])
        event.save()

        #cause from event model is null
        
        return redirect(reverse("user:ManageEvents"))
    
    context = {
        "event": event,
    }

    return render(request, "AddEvent.html", context)


@login_required(login_url="/Login")
def delete_event(request, id):

    event = get_object_or_404(Event, pk=id)
    event.delete()

    return redirect(reverse("user:ManageEvents"))


@login_required(login_url="/Login")
def manage_stories(request):
    
    stories = SuccessStory.objects.all()
    context = {
        "stories": stories
    }

    return render(request, "ManageStories.html", context)


@login_required(login_url="/Login")
def add_story(request):

    if request.method == "POST":
        story:SuccessStory = SuccessStory()

        story.title = request.POST["title"]
        story.content = request.POST["body"]
        story.summery = request.POST["summery"]

        if request.FILES:
            story.image = request.FILES["display_image"]

        story.save()

        return redirect(reverse("user:ManageStories"))

    return render(request, "AddStory.html", {})


@login_required(login_url="/Login")
def edit_story(request, id):

    story = get_object_or_404(SuccessStory, pk=id)

    if request.method == "POST":

        story.title = request.POST["title"]
        story.content = request.POST["body"]
        story.summery = request.POST["summery"]

        if request.FILES:
            story.image = request.FILES["display_image"]

        story.save()

        return redirect(reverse("user:ManageStories"))

    return render(request, "AddStory.html", {"story": story})


@login_required(login_url="/Login")
def delete_story(request, id):

    story = get_object_or_404(SuccessStory, pk=id)

    story.delete()
    
    return redirect(reverse("user:ManageStories"))
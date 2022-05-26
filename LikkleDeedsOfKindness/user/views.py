from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from cause.models import Cause
from project.models import Project, ProjectImage

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

def cause_projects(request, id):
    
    projects =  Project.objects.filter(cause=id) 

    context = {
        "projects" : projects,
        "cause": id,
        
    }

    return render(request, "CauseProjects.html", context)

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

def project_images(request, id):

    images = ProjectImage.objects.filter(project=id)
    
    context = {
        "images": images
    }
    return render(request, "ProjectImages.html", context)

def edit_image(request, id):

    if request.method == "POST":
        project_image:ProjectImage = ProjectImage.objects.get(pk=id)

        project_image.caption = request.POST["caption"]

        if request.FILES:
            project_image.image = request.FILES["image"]
        
        project_image.save()

    return redirect(reverse("user:ProjectImages", args=[project_image.project.pk]))
    





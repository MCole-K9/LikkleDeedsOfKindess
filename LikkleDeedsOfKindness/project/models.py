from django.db import models
from cause.models import Cause
import random, re
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    video_link = models.CharField(max_length=225, default="none")
    display_image = models.ImageField(upload_to="images/" , default="none")

    def __str__(self):
        return self.title

    def get_image(self):
        """"Return a Random project image(model)"""
        project_images = ProjectImage.objects.filter(project=self.id)
        project_image = random.choice(project_images)
        return project_image

    def get_images(self):
        return ProjectImage.objects.filter(project=self.id)
    
    def get_embed_link(self) -> str:
        """Transforms the the video link to an acceptable format form an embed video link for the respective hosts"""
        
        if re.search("youtube.com", self.video_link): 
            url_parts = re.split("//", self.video_link)

            yt_link = url_parts[1]
            yt_link_parts = re.split("/", yt_link)
            yt_link_parts.insert(1, "embed")
            yt_link = "/".join(yt_link_parts) 

            url_parts[1] = yt_link

            embed_url = "//".join(url_parts)
            return embed_url

    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    caption = models.CharField(max_length=225)

class ProjectVideo(models.Model):
    video_link = models.CharField(max_length=225)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

from django.db import models

# Create your models here.

class ProjectDetail(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='projects_img/')
    description = models.TextField(max_length=500)
    github_url = models.URLField(max_length=200)
    live_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name.title()
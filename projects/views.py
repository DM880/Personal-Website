from django.shortcuts import render
from website.views import *
from .models import *

# Create your views here.

def base_project(request):

    all_projects_info = ProjectDetail.objects.all()

    all_projects = []

    for proj_info in all_projects_info:

        all_projects.append(proj_info)

    return render(request, "base_project.html", {'all_projects':all_projects})
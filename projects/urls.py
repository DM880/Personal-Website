from django.urls import path, include
from .views import *

app_name = "project"

urlpatterns = [
                path('', base_project, name="base_project"),
                ]
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.resume_index, name="resume_index"),
    path("resume/projects", views.resume_projects, name="resume_projects"),
    path("resume/demo", views.resume_demo, name="resume_demo"),
]
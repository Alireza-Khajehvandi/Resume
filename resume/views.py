from django.shortcuts import render
from django.http import HttpResponse
import datetime


def resume_index(request):
    return render(request, "resume/resume_index.html")

def resume_projects(request):
    return render(request, "resume/resume_projects.html")


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from resume.models import Project
from django.db.models import Q

# Create your views here.


def website_index(request):
    return render(request, "website/website_index.html")

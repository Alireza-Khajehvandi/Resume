from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index_resume(request):
    return render(request, "resume/index_resume.html")

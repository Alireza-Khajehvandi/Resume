from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from resume.models import Projects
from django.db.models import Q


def resume_index(request):
    projects = Projects.objects.filter(status=1)
    context = {"projects": projects}
    return render(request, "resume/resume_index.html", context)


def resume_projects(request, cat_name=None):
    projects = Projects.objects.filter(status=1)
    if cat_name:
        projects = projects.filter(category__name=cat_name)
    context = {"projects": projects}
    return render(request, "resume/resume_projects.html", context)


def resume_demo(request):
    return render(request, "resume/demo.html")


def resume_test(request, pid=None):
    projects = Projects.objects.filter(status=1)
    context = {"projects": projects}
    return render(request, "resume/test.html", context)

# def resume_category(request, cat_name):
#     projects = Projects.objects.filter(status=1)
#     projects = projects.filter(category__name=cat_name)
#     context = {"projects": projects}
#     return render(request, "resume/resume_projects.html", context)


def resume_search(request):
    # print(request.__dict__)
    projects = Projects.objects.filter(status=1)
    if request.method == "GET":
        # print(request.GET.get("s"))
        if s := request.GET.get("s"):
            if projects.filter(content__contains=s):
                projects = projects.filter(content__contains=s)
            if projects.filter(title__contains=s):
                projects = projects.filter(title__contains=s)

    context = {"projects": projects}
    return render(request, "resume/resume_projects.html", context)

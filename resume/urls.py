from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.resume_index, name="resume_index"),
    path("resume/projects", views.resume_project, name="resume_projects"),
    path("resume/projects/category/<str:cat_name>", views.resume_project, name="resume_category"),
    path("resume/projects/search/", views.resume_search, name="resume_search"),
    # path("resume/projects/<int:pid>", views.resume_project_id, name="resume_project_id"),
    path("resume/demo", views.resume_demo, name="resume_demo"),
    path("resume/test", views.resume_test, name="resume_test"),
]

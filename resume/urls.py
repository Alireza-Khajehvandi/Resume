from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index_resume, name="index_resume"),
    
]
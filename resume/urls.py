from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.current_datetime, name="index"),
    
]
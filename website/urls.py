from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("website", views.website_index, name="website_index"),
]

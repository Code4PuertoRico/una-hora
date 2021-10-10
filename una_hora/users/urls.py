from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path("<str:pag>", views.last_twelve, name="last_twelve"),
]
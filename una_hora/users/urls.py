from django.urls import path

from . import views

urlpatterns = [
    path("<str:pag>", views.last_twelve, name="last_twelve"),
]

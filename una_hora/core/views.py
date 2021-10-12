from django.shortcuts import render  # noqa: F401
from django.http import HttpResponse


def legal(request):
    return render(request, "This is the legal page")

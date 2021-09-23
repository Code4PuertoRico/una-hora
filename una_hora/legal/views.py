from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def legal(request):
    return HttpResponse("This is the legal page")

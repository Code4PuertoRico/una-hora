from django.shortcuts import render  # noqa: F401

def legal(request):
    return render(request, "legal.html")

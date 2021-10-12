from django.shortcuts import render  # noqa: F401


def legal(request):
    return render(request, "This is the legal page")

from django.contrib.auth.decorators import login_required
from .models import User
from django.core.paginator import Paginator
from django.shortcuts import render

def last_twelve(request):
    last_users = User.objects.filter(is_active=True)
    last_users = last_users.order_by("-date_joined").all()
    paginator = Paginator([last_user.serialize() for last_user in last_users],12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_items = len(page_obj)
    return render(request, "common/pagination.html", {'page_obj': page_obj,'page_items':page_items})
from django.contrib.auth.views import LoginView
from django.urls import path

from .views import ProfileView, SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile"),
]

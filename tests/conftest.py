import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
@pytest.mark.django_db
def user():
    email = "test_email@example.com"
    password = "test_password"
    user = User.objects.create(email=email, password=password)
    return user

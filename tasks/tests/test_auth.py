import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_login():
    user = User.objects.create_user(
        username="testuser",
        password="testpass123"
    )

    client = APIClient()
    response = client.post("/api/auth/login/", {
        "username": "testuser",
        "password": "testpass123"
    })

    assert response.status_code == 200
    assert "access" in response.data

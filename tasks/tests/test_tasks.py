import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tasks.models import Task, Category


@pytest.mark.django_db
def test_create_and_complete_task():
    client = APIClient()

    user = User.objects.create_user(
        username="testuser",
        password="testpwd123"
    )

    # Login
    login = client.post("/api/auth/login/", {
        "username": "testuser",
        "password": "testpwd123"
    })

    access = login.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

    # Crear categoría
    category, created = Category.objects.get_or_create(name="Trabajo")

    # Crear tarea
    response = client.post("/api/tasks/", {
        "title": "Tarea test",
        "description": "Descripción de tarea test",
        "category_id": category.id
    })

    print(response.data)
    assert response.status_code == 201
    task_id = response.data["id"]

    # Ver pendientes
    pending = client.get("/api/tasks/?status=pending")
    assert len(pending.data["results"]) == 1

    # Finalizar tarea
    complete = client.patch(f"/api/tasks/{task_id}/complete/")
    assert complete.data["status"] == Task.STATUS_DONE

    # Ya no aparece en pendientes
    pending = client.get("/api/tasks/?status=pending")
    assert len(pending.data["results"]) == 0

    # Aparece en finalizadas
    done = client.get("/api/tasks/?status=done")
    assert len(done.data["results"]) == 1

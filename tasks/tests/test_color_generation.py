import pytest
from django.contrib.auth import get_user_model
from tasks.models import Task, Category

User = get_user_model()

@pytest.mark.django_db
def test_color_is_unique():
    user = User.objects.create_user(username="testuser", password="1234")
    
    category = Category.objects.create(name="Cat1")

    task = Task.objects.create(
        title="T1",
        description="Test description",
        status="pending",
        color="#FFFFFF",
        category_id=category.id,
        user_id=user.id
    )

    assert task.color == "#FFFFFF"

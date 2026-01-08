from django.db import models
from django.conf import settings
import uuid


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_DONE = 'done'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_DONE, 'Finalizada'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    color = models.CharField(max_length=7)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from rest_framework import serializers
from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            "required": "El nombre de la categoría es obligatorio.",
            "blank": "El nombre de la categoría no puede estar vacío.",
            "max_length": "El nombre de la categoría no puede exceder los 50 caracteres."
        }
    )

    class Meta:
        model = Category
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):

    title = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
        error_messages={
            "required": "El título es obligatorio.",
            "blank": "El título no puede estar vacío.",
            "max_length": "El título no puede exceder los 255 caracteres."
        }
    )

    description = serializers.CharField(
        required=False,
        allow_blank=False,
        max_length=1000,
        error_messages={
            "blank": "La descripción no puede estar vacía.",
            "max_length": "La descripción no puede exceder los 1000 caracteres."
        }
    )

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        error_messages={
            "does_not_exist": "La categoría seleccionada no existe.",
            "required": "La categoría es obligatoria."
        },
        write_only=True
    )

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'color',
            'category',
            'category_id',
            'created_at',
        ]
        read_only_fields = ['id', 'color', 'created_at']

class TaskCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']
        read_only_fields = ['status']

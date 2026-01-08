from django.db import migrations


def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('tasks', 'Category')

    categories = [
        'Trabajo',
        'Estudio',
        'Casa',
        'Familia',
        'Diversión',
    ]

    for name in categories:
        Category.objects.get_or_create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]

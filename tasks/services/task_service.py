import random
from tasks.models import Task

def generate_unique_color():
    used_colors = set(Task.objects.values_list('color', flat=True))

    while True:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if color not in used_colors:
            return color

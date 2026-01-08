from django.urls import path
from .views import (
    TaskListCreateView,
    TaskDeleteView,
    TaskCompleteView,
    CategoryCreateListView
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<uuid:pk>/delete/', TaskDeleteView.as_view()),
    path('tasks/<uuid:pk>/complete/', TaskCompleteView.as_view()),
    path('categories/', CategoryCreateListView.as_view()),
]

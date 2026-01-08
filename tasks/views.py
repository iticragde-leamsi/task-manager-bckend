from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from .services.task_service import generate_unique_color
from .pagination import TaskPagination


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination

    def get_queryset(self):
        status_param = self.request.query_params.get('status')
        queryset = Task.objects.filter(user=self.request.user, is_deleted=False).order_by('-created_at')

        if status_param in [Task.STATUS_PENDING, Task.STATUS_DONE]:
            queryset = queryset.filter(status=status_param)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = Task.STATUS_DONE
        task.save()
        return Response(TaskSerializer(task).data)


class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


class TaskCompleteView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = Task.STATUS_DONE
        task.save()
        return Response(TaskSerializer(task).data)

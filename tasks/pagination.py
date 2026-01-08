import environ
from rest_framework.pagination import PageNumberPagination

env = environ.Env()

class TaskPagination(PageNumberPagination):
    page_size = env.int("TASK_PAGE_SIZE", default=6)
    page_size_query_param = 'page_size'
    max_page_size = env.int("TASK_MAX_PAGE_SIZE", default=20)

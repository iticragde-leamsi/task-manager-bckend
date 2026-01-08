from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from tasks.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/logout/', LogoutView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),  
    path('api/', include('tasks.urls')),
]

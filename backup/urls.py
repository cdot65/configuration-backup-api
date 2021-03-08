from django.urls import path, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from backup import views
from backup.views import BackupViewSet, UserViewSet, api_root, DeleteViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'backups', views.BackupViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('delete/', views.DeleteViewSet.as_view()),
]

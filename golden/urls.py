from django.urls import path, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from golden import views
from golden.views import GoldenViewSet, UserViewSet, api_root, DeleteViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'configs', views.GoldenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('delete/', views.DeleteViewSet.as_view()),
]

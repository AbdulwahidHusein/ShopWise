from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter()
router.register('', CustomUserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls), name='accounts-list'),
]
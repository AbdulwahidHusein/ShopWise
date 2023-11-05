from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

app_name = 'accounts'

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls), name='accounts-list'),
]
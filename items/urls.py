from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemView

app_name = 'items'
router = DefaultRouter()
router.register("", ItemView, basename="item")

urlpatterns = [
    path("", include(router.urls), name="items"),
]
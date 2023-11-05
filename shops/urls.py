from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ShopViewSet

app_name = "shops"

router = DefaultRouter()
router.register("", ShopViewSet, basename="shops")


urlpatterns = [
    path("", include(router.urls), name="shops"),
]

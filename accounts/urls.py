from django.urls import path
from .views import CustomUserView

app_name = 'accounts'

urlpatterns = [
    path('list', CustomUserView.as_view({'get': 'list', 'post': 'create'}), name='accounts-list'),
    path('account/<int:pk>/', CustomUserView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='accounts-detail'),
]
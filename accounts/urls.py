from django.urls import path
from .views import CustomUserView

app_name = 'accounts'

urlpatterns = [
    path('accounts', CustomUserView.as_view({'get': 'list', 'post': 'create'}), name='accounts-list'),
    path('accounts/<int:pk>/', CustomUserView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='accounts-detail'),
]
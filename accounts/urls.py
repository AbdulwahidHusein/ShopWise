from django.urls import path
from .views import CustomUserView

app_name = 'accounts'

urlpatterns = [
    path('accounts_list', CustomUserView.as_view({'get': 'list'}), name='accounts-list'),
    path('account/<int:pk>/', CustomUserView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='accounts-detail'),
]
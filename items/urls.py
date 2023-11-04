from django.urls import path
from .views import ItemView

app_name = 'items'

urlpatterns = [
    path('list', ItemView.as_view({'get': 'list', 'post': 'create'}), name='accounts-list'),
    path('item/<int:pk>/', ItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='accounts-detail'),
]
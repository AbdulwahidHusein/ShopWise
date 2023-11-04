from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
# Create your views here.


class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
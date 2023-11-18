from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserLoginSerializer, CustomUserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action

class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
from django.db import transaction   
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserRegistrationSerializer, CustomUserLoginSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'login':
            return CustomUserLoginSerializer
        elif self.action == 'register':
            return CustomUserRegistrationSerializer
        else:
            return CustomUserSerializer
    @transaction.atomic
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.username,
        })
    @transaction.atomic
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    @transaction.atomic
    def perform_create(self, serializer):
        user = serializer.save()
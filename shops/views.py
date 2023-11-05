from .models import Shop
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ShopSerializer
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import action

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    authentication_classes = [JWTAuthentication]
    queryset = Shop.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_permissions(self):
        permission_classes = []
        if self.request.method in ['DELETE', 'PUT', 'PATCH', 'POST']:
            permission_classes.append(permissions.IsAuthenticated)
            # Allow only the item creator to delete, update, or partially update the item
            #permission_classes.append(IsUserItemOwner)
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        user = self.request.user
        try:
            serializer.save(seller=user)
        except ObjectDoesNotExist:
            return Response("can't create a shop")
    
    
    
    
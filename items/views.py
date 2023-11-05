from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import  permissions
from custom_permissions import IsUserItemOwner
# Create your views here.

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'retrieve':
            # Allow unauthenticated access for GET requests (retrieve method)
            return []
        if self.request.method in ['DELETE', 'PUT', 'PATCH']:
            # Allow only the item creator to delete, update, or partially update the item
            permission_classes = [IsUserItemOwner]
        else:
            # Require authentication for all other methods
            permission_classes = [permissions.IsAuthenticated]
            return [permission() for permission in permission_classes]
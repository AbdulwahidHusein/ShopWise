from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import  permissions
from custom_permissions import IsUserItemOwner
from shops.models import Shop
# Create your views here.

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.request.method in ['DELETE', 'PUT', 'PATCH']:
            permission_classes.append(permissions.IsAuthenticated)
            # Allow only the item creator to delete, update, or partially update the item
            permission_classes.append(IsUserItemOwner)
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        user_id = self.request.user.id
        user_shop = Shop.objects.get(seller__id = user_id)
        serializer.save(shop=user_shop)
        
    # def get_queryset(self):
    #     # Filter the queryset to show only items created by the authenticated user
    #     user = self.request.user
    #     return Item.objects.filter(shop__seller=user)
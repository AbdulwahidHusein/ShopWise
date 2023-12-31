from .models import Shop
from accounts.models import Seller
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ShopSerializer
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import IntegrityError
from custom_permissions import IsUserShopOwner
from items.serializers import ItemSerializer
from django.db import transaction

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    authentication_classes = [JWTAuthentication]
    queryset = Shop.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_permissions(self):
        permission_classes = []
        if True:
            permission_classes.append(permissions.IsAuthenticated)
            # Allow only the item creator to delete, update, or partially update the item
            permission_classes.append(IsUserShopOwner)
        return [permission() for permission in permission_classes]
    @transaction.atomic
    def perform_create(self, serializer):
        user = self.request.user
        try:
            with transaction.atomic():
                seller = Seller.objects.select_for_update.get(profile=user)
                try:
                    serializer.save(seller=seller)
                except IntegrityError:
                    return Response("you already have a shop opened")
        except ObjectDoesNotExist:
            return Response("first create seller profile before creating a shop")
    def get_queryset(self):
        user_id = self.request.user.id
        return Shop.objects.filter(seller__profile__id = user_id)
    
    @action(detail=False, methods=['GET'], authentication_classes=[JWTAuthentication], permission_classes=[permissions.IsAuthenticated])
    def get_all_items(self, request):
        user_id = self.request.user.id
        shop = Shop.objects.filter(seller__profile__id=user_id).first()
        if not shop:
            return Response([])
        items = shop.shop_items.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    
    
    
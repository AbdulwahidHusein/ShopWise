from rest_framework import serializers
from items.serializers import ItemSerializer
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    shop_items = ItemSerializer(many=True, read_only=True)  # Nested serializer for the related items
    class Meta:
        model = Shop
        fields = ('catagory', 'shop_items')
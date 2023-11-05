from rest_framework import serializers
from .models import Item, ItemImage

class ItemImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ItemImage
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, required=False)
    class Meta:
        model = Item
        fields = '__all__'
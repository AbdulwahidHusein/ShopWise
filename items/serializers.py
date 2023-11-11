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
    
    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        item = Item.objects.create(**validated_data)

        for image_data in images_data:
            ItemImage.objects.create(item=item, image=image_data)

        return item
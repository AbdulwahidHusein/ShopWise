from django.db import models
from shops.models import Shop
# Create your models here.

class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, related_name="shop_items", null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=50, default="unsold")
    
    def __str__(self) -> str:
        return self.shop.seller.profile.username + "'s shop item"
    
class ItemImage(models.Model):
    image = models.ImageField(upload_to="items/item_images", null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")
    
    def __str__(self) -> str:
        return self.item.shop.seller.profile.username + "'s item image"
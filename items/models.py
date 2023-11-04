from django.db import models
from shops.models import Shop
# Create your models here.

class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop")
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    status = models.CharField(max_length=50)
    
class ItemImage(models.Model):
    image = models.ImageField(upload_to="items/images", null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
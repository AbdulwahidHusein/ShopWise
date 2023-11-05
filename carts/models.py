from django.db import models
from accounts.models import Buyer
from items.models import Item
# Create your models here.

class Cart(models.Model):
    buyer = models.OneToOneField(Buyer, related_name="seller", on_delete=models.PROTECT)
    items = models.ManyToManyField(Item, related_name='items')
    def __str__(self) -> str:
        return self.buyer.profile.email
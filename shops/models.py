from django.db import models
from accounts.models import Seller
# Create your models here.

class Shop(models.Model):
    CHOICE_A = 'A'
    CHOICE_B = 'B'
    CHOICE_C = 'C'

    catagories = [
        (CHOICE_A, 'catagory a'),
        (CHOICE_B, 'catagory b'),
        (CHOICE_C, 'catagory c'),
    ]
    catagory = models.CharField(max_length=100, choices=catagories)
    seller = models.OneToOneField(Seller, related_name="seller", on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.seller.profile.email +" "+ self.catagory
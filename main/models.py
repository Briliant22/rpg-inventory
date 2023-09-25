from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    power = models.IntegerField()
    price = models.IntegerField()
    amount = models.IntegerField()
    
    CATEGORY_CHOICES = [
        ("Weapons", "Weapons"),
        ("Armors", "Armors"),
        ("Consumables", "Consumables"),
        ("Magic Items", "Magic Items"),
        ("Miscellaneous", "Miscellaneous"),
    ]

    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    description = models.TextField()


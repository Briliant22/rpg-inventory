from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    power = models.IntegerField()
    category = models.CharField(max_length=255)
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    price = models.FloatField()
    sale = models.BooleanField()

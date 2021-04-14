from django.db import models

# Create your models here.
from buyers.models import Buyer


class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return f"{self.name}-{self.price}-{self.buyer}"
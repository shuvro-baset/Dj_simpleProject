from django.db import models
from cars.models import Car
# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=200)
    cars = models.ManyToManyField(Car)
    total = models.PositiveIntegerField(blank=True)
    total_price = models.PositiveIntegerField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
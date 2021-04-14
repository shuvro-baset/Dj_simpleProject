from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Sale
from orders.models import Order

@receiver(pre_delete, sender=Sale)
def pre_delete_change_active_order(sender, instance, **kwargs):
    obj = instance.order
    obj.active= False
    obj.save()
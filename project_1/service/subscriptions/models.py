from django.db import models
from accounts.models import CustomUser


# Create your models here.
class Tariff(models.Model):
    price = models.DecimalField(null=False, blank=False, max_digits=6, decimal_places=2)
    name = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name="subscriptions")
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True, related_name="subscriptions")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

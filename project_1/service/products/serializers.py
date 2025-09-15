from rest_framework import serializers

from accounts.models import CustomUser
from products.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["customer", "products"]


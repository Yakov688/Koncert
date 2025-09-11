from rest_framework import serializers

from accounts.models import CustomUser
from products.models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Order
        fields = ["customer", "products"]


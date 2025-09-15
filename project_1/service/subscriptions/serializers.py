from subscriptions.models import UserSubscription, Tariff
from rest_framework import serializers


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ["user", "tariff", "is_active"]


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = "__all__"

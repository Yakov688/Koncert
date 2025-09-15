# Create your views here.
from subscriptions.serializers import UserSubscriptionSerializer, TariffSerializer
from rest_framework import viewsets
from subscriptions.models import Tariff, UserSubscription


class TariffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class UserSubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = UserSubscriptionSerializer
    queryset = UserSubscription.objects.select_related('user').select_related('tariff').only(
        'is_active',
        'user__username',
        'tariff__name'
    )



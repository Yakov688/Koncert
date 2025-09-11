from django.db.models import Prefetch
from rest_framework import viewsets, status
from rest_framework.response import Response
import logging

from accounts.models import CustomUser
from products.models import Order, Product
from products.serializers import OrderSerializer
from telegram_bot import send_notification

logger = logging.getLogger(__name__)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related(
        Prefetch('products', queryset=Product.objects.only('name')),
        Prefetch('customer', queryset=CustomUser.objects.only('username', 'telegram_id'))
    )
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = serializer.save()

        self.send_telegram_notification(order)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def send_telegram_notification(self, order):
        print(f"🔔 Отправка уведомления для заказа {order.id}")

        if not order.customer:
            return False

        if order.customer.telegram_id:
            message = f"Вам пришёл новый заказ №{order.id}!"
            success = send_notification(order.customer.telegram_id, message)
            return success
        else:
            print("❌ Нет telegram_id для отправки уведомления")
            return False

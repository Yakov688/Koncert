from django.contrib import admin

from subscriptions.models import Tariff, UserSubscription

# Register your models here.
admin.site.register(Tariff)
admin.site.register(UserSubscription)

from django import forms
from subscriptions.models import UserSubscription


class UserSubscriptionForm(forms.ModelForm):
    class Meta:
        model = UserSubscription
        fields = ['user', 'tariff', 'is_active']

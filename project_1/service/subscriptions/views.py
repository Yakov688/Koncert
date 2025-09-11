

# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from subscriptions.forms import UserSubscriptionForm
from subscriptions.models import Tariff, UserSubscription


class TariffListView(ListView):
    model = Tariff
    context_object_name = 'tariffs'
    template_name = 'tariff_list.html'


class UserSubscriptionDetailView(DetailView):
    model = UserSubscription
    template_name = 'user_subscription_details.html'
    context_object_name = 'subscription'


class UserSubscriptionCreateView(CreateView):
    model = UserSubscription
    form_class = UserSubscriptionForm
    template_name = 'new_subscription_form.html'
    success_url = reverse_lazy('subscriptions_list')


class UserSubscriptionListView(ListView):
    model = UserSubscription
    context_object_name = 'subscriptions'
    template_name = 'user_subscription_list.html'
    queryset = UserSubscription.objects.select_related('tariff').select_related('user').all()


class UserSubscriptionUpdateView(UpdateView):
    model = UserSubscription
    form_class = UserSubscriptionForm
    template_name = 'user_subscription_update.html'
    context_object_name = 'subscription'

    def get_success_url(self):
        return reverse_lazy('subscription_details', kwargs={'pk': self.object.pk})


class UserSubscriptionDeleteView(DeleteView):
    model = UserSubscription
    template_name = 'user_subscription_delete.html'
    success_url = reverse_lazy('subscriptions_list')
    context_object_name = 'subscription'

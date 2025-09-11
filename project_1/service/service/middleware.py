from django.http import HttpResponseRedirect, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from subscriptions.models import UserSubscription
from django.urls import reverse


class IsActiveMiddleware(MiddlewareMixin):
    def process_request(self, request):
        specific_paths = ['/api/order/']

        if request.path in specific_paths:
            if request.user.is_authenticated:
                current_user = UserSubscription.objects.get(user=request.user)
                if not current_user.is_active:
                    return JsonResponse({'error': 'Your subscription is inactive.'}, status=403)
            else:
                return HttpResponseRedirect(reverse('login'))
        return None

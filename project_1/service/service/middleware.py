from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from subscriptions.models import UserSubscription


class IsActiveMiddleware(MiddlewareMixin):
    def process_request(self, request):
        specific_paths = ['/api/order/']

        if request.path in specific_paths:
            if request.user.is_authenticated:
                current_user = UserSubscription.objects.get(user=request.user)
                if not current_user.is_active:
                    return JsonResponse({'error': 'Your subscription is inactive.'}, status=403)
            else:
                login_url = f'/api/auth/login/?next={request.path}'
                return redirect(login_url)
        return None

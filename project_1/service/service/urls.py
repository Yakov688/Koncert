"""
URL configuration for service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


from rest_framework import routers

from subscriptions.views import (
    TariffListView,
    UserSubscriptionCreateView,
    UserSubscriptionListView,
    UserSubscriptionDetailView,
    UserSubscriptionUpdateView,
    UserSubscriptionDeleteView,
)

from products.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tariffs/', TariffListView.as_view(), name='tariffs'),

    path('new_subscription/', UserSubscriptionCreateView.as_view()),
    path('subscription_details/<int:pk>/', UserSubscriptionDetailView.as_view(), name='subscription_details'),
    path('subscriptions/', UserSubscriptionListView.as_view(), name='subscriptions_list'),
    path('subscription/<int:pk>/update/', UserSubscriptionUpdateView.as_view(), name='update_subscription'),
    path('subscription/<int:pk>/delete/', UserSubscriptionDeleteView.as_view(), name='delete_subscription'),

    path('api/', include(router.urls)),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

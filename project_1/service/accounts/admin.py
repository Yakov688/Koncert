from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

admin.site.register(CustomUser, UserAdmin)

UserAdmin.fieldsets += (('Custom fields set', {'fields': ['phone', 'telegram_id']}),)

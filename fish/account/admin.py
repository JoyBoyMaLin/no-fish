from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User
from django.utils.translation import gettext_lazy


class AdminUser(UserAdmin):
    list_display = ('full_name', 'phone_number', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login')
    search_fields = ('full_name', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        (gettext_lazy('User Information'), {'fields': ('full_name', 'phone_number', 'date_of_birth', 'avatar')}),

        (gettext_lazy('Permissions'),
         {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('id',)


admin.site.register(User, AdminUser)
admin.site.site_header = '混沌麟后台管理'
admin.site.site_title = '后台管理'

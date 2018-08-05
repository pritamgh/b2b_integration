from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

"""from django_object_actions import (
    DjangoObjectActions,
)

from django.utils.translation import ugettext_lazy as _


@admin.register(CustomUser)
class CustomUserAdmin(DjangoObjectActions, UserAdmin):

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password'
            )
        }),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'username',
            ),
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        (_('Important dates'), {
            'fields': (
                'last_login',
                'date_joined'
            )
        }),
    )
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    )


    class Media:
        js = (
            'js/admin/reports/pico-modal.js',
            'js/admin/reports/pico-modal-init.js',
        )
        css = {
            'all': (
                'css/admin/reports/pico-modal.css',
            )
        }

    def _avatar(self, user):
        if user.avatar:
            return format_html(mark_safe(
                "<img src='{}' >".format(user.avatar.url)))
        else:
            return "None" """

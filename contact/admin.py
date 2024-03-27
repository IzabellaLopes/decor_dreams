"""Contact Admin"""

from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Allows admin to manage contact via the admin panel"""
    list_display = (
        'name',
        'email',
        'consultation',
        'date',
    )


admin.site.register(Contact, ContactAdmin)
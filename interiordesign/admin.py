"""Interior Design Admin"""

from django.contrib import admin
from .models import Design


class DesignAdmin(admin.ModelAdmin):
    """Allows admin to manage interior design services via the admin panel"""
    list_display = (
        'type',
        'description',
        'image',
    )


admin.site.register(Design, DesignAdmin)
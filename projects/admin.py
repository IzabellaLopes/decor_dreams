"""Projects Admin"""

from django.contrib import admin
from .models import PreviousProject


class PreviousProjectAdmin(admin.ModelAdmin):
    """Allows admin to manage Previous Projects via the admin panel"""
    list_display = (
        'design',
        'location',
        'image',
    )


admin.site.register(PreviousProject, PreviousProjectAdmin)
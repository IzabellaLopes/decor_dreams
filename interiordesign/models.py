"""Interior Design Models"""

from django.db import models
from django.urls import reverse


class Design(models.Model):
    """ Model for Interior Design Service """
    type = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        """Get url after superuser adds/edits interior design service"""
        return reverse('interiordesign')

"""Projects Models"""

from django.db import models
from django.urls import reverse
from interiordesign.models import Design


class PreviousProject(models.Model):
    """Model for previous projects"""
    design = models.ForeignKey(
        Design, on_delete=models.CASCADE, related_name='previous_project')
    image = models.ImageField(null=True, blank=False)
    location = models.CharField(max_length=254)

    def get_absolute_url(self):
        """Get url after user adds project image"""
        return reverse('project_gallery')

    def __str__(self):
        return f"Project: {self.design} in {self.location}"
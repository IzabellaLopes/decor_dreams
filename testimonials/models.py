"""Testimonials Models"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from interiordesign.models import Design


class Testimonial(models.Model):
    """Model for Testimonials"""
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='testimonials')
    design = models.ForeignKey(
        Design, on_delete=models.CASCADE, related_name='testimonial')
    message = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ To display the testimonials by created_on in ascending order """
        ordering = ['created_on']

    def get_absolute_url(self):
        """Get url after user adds/edits testimonials"""
        return reverse('testimonials')

    def __str__(self):
        return f"Testimonial: {self.design} by {self.name}"
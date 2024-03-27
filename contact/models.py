""" Contact Models """

from django.db import models
from django.urls import reverse


class Contact(models.Model):
    """ Model for Contact """

    DESIGN_CONSULTATION = 'DS'
    PRODUCT_QUERY = 'PQ'
    ORDER_QUERY = 'OQ'
    OTHER = 'O'
    CONSULTATION_CHOICES = [
        ('DESIGN_CONSULTATION', 'Interior Design Service'),
        ('PRODUCT_QUERY', 'Product Query'),
        ('ORDER_QUERY', 'Order Query'),
        ('OTHER', 'Other')
        ]

    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    consultation = models.CharField(
        max_length=254, choices=CONSULTATION_CHOICES, default='DS')
    message = models.TextField(max_length=500, default='')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Get url after user submits consultation """
        return reverse('home')

    class Meta:
        """ To display the consultations by date in ascending order """
        ordering = ['-date']

    def __str__(self):
        return f"Schedule a consultation: {self.consultation} from {self.name}"
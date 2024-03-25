"""Interior Design Views"""

from django.views import generic
from .models import Design


class Design(generic.ListView):
    """ This view is used to display all interior design services """
    model = Design
    template_name = 'interiordesign/interiordesign.html'
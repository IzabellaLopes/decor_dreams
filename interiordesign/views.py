"""Interior Design Views"""

from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Design
from .forms import DesignForm



class Design(generic.ListView):
    """ This view is used to display all interior design services """
    model = Design
    template_name = 'interiordesign/interiordesign.html'
    

class AddDesign(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.CreateView):

    """This view is used to allow site owner to add a new interior design service"""
    form_class = DesignForm
    template_name = 'interiordesign/add_design.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the service type into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.type,
        )

    def test_func(self):
        """
        Ensures only superuser can add new services
        """
        if self.request.user.is_superuser:
            return True
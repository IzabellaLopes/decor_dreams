"""Interior Design Views"""

from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Design
from .forms import DesignForm


class DesignListView(generic.ListView):
    """
    This view is used to display all interior design services
    """
    model = Design
    template_name = 'interiordesign/interiordesign.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class DesignCreateView(LoginRequiredMixin,
                       UserPassesTestMixin,
                       SuccessMessageMixin,
                       generic.CreateView):
    """
    This view is used to allow the site owner to add an interior design service
    """
    form_class = DesignForm
    template_name = 'interiordesign/add_design.html'
    success_message = "%(calculated_field)s was created successfully"
    success_url = reverse_lazy('interiordesign')

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted
        """
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the interior design service type into the success message
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.type,
        )

    def test_func(self):
        """
        Ensures only superuser can add a new interior design service
        """
        return self.request.user.is_superuser


class DesignUpdateView(LoginRequiredMixin,
                       UserPassesTestMixin,
                       SuccessMessageMixin,
                       generic.UpdateView):
    """
    This view is used to allow the superuser to edit an interior design service
    """
    model = Design
    form_class = DesignForm
    template_name = 'interiordesign/edit_design.html'
    success_message = "%(calculated_field)s was edited successfully"
    success_url = reverse_lazy('interiordesign')

    def test_func(self):
        """
        Ensure only superuser can edit an interior design service details
        """
        return self.request.user.is_superuser

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to edit
        the interior design service type into the success message
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.type,
        )


class DesignDeleteView(LoginRequiredMixin,
                       UserPassesTestMixin,
                       generic.DeleteView):
    """
    This view is used to allow the superuser to delete
    an interior design service
    """
    model = Design
    template_name = 'interiordesign/delete_design.html'
    success_url = reverse_lazy('interiordesign')

    def test_func(self):
        """
        Ensure only superuser can delete a service
        """
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display success message given
        SuccessMessageMixin cannot be used in generic.DeleteView.
        """
        messages.success(self.request,
                         "Successfully deleted interior design service!")
        return super().delete(request, *args, **kwargs)
"""Projects Views"""

from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import PreviousProject
from django.urls import reverse_lazy
from .forms import AddProjectImageForm


class ProjectGallery(generic.ListView):
    """ This view is used to display photo gallery of previous projects """
    model = PreviousProject
    template_name = 'projects/project_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddProjectImage(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.CreateView):
    """
    This view is used to allow the site owner to add
    images of previous projects to the gallery
    """
    form_class = AddProjectImageForm
    template_name = 'projects/add_project_image.html'
    success_message = "Your image was added successfully"

    def test_func(self):
        """
       Ensure only superuser can add an image
        """
        if self.request.user.is_superuser:
            return True


class DeleteProjectImage(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow the superuser to delete images from the gallery
    """
    model = PreviousProject
    template_name = 'projects/delete_project_image.html'
    success_message = "Project successfully deleted"
    success_url = reverse_lazy('project_gallery')

    def test_func(self):
        """
       Ensure only superuser can delete an image
        """
        if self.request.user.is_superuser:
            return True

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteProjectImage, self).delete(request, *args, **kwargs)
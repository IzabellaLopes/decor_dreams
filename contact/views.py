"""Contact Views"""

from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.views import generic, View
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import Contact


class ContactUs(View):
    """
    This view is used to display the contact form and
    handle GET and POST requests
    """

    def get(self, request):
        """
        Renders the contact form
        """
        if request.user.is_authenticated:
            form = ContactForm(initial={'email': request.user.email})
        else:
            form = ContactForm()

        return render(
            request,
            "contact/contact.html",
            {"contact_form": form},
        )

    def post(self, request):
        """
        This method is called when a POST request is made to the view
        via the contact form
        """
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save()
            cust_name = contact.name
            cust_email = contact.email
            subject = contact.consultation
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'subject': subject})
            message = contact.message
            message = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'cust_name': cust_name, 'message': message}
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )

            messages.success(request, "Your consultation has been sent")

            return redirect("home")

        else:
            messages.error(request,
                           "Form failed. Please ensure the form is valid"
                           )

            return render(request,
                          "contact/contact.html",
                          {"plain_message": True, "contact_form": contact_form}
                          )


class Consultation(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """ This view is used to display all consultations """
    model = Contact
    template_name = 'contact/consultation_dashboard.html'

    def test_func(self):
        """
        Ensures only superuser can view consultations
        """
        return self.request.user.is_superuser


class ConsultationDetail(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DetailView
    ):
    """ This view is used to display selected consultation detail """
    model = Contact
    template_name = 'contact/consultation_detail.html'

    def test_func(self):
        """
        Ensures only superuser can add view consultations
        """
        return self.request.user.is_superuser

class DeleteConsultation(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
    ):
    """
    This view is used to allow the superuser to delete a consultation
    """
    model = Contact
    template_name = 'contact/delete_consultation.html'
    success_message = "Consultation deleted successfully"

    def test_func(self):
        """
        Ensure only superuser can edit service details
        """
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display success message given
        SuccessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Get the success URL dynamically using reverse
        """
        return reverse("consultation")
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUs.as_view(), name='contact'),
    path('consultation/', views.Consultation.as_view(), name='consultation'),
    path(
        'confirmation/', views.ContactConfirmation.as_view(),
         name='confirmation'
         ),
    path(
        'consultation/<int:pk>/',
        views.ConsultationDetail.as_view(), name='consultation_detail'
        ),
    path(
        'consultation/delete/<int:pk>/', views.DeleteConsultation.as_view(),
        name='delete_consultation'
        ),
]
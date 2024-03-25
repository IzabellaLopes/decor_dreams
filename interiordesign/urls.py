from django.urls import path
from . import views

urlpatterns = [
    path('', views.Design.as_view(), name='interiordesign'),
]
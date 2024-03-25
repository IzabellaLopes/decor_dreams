from django.urls import path
from . import views

urlpatterns = [
    path('', views.Design.as_view(), name='interiordesign'),
    path('add/', views.AddDesign.as_view(), name='add_design'),

]
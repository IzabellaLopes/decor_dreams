from django.urls import path
from . import views

urlpatterns = [
    path('', views.DesignListView.as_view(), name='interiordesign'),
    path('add/', views.DesignCreateView.as_view(), name='add_design'),
    path('edit/<int:pk>/', views.DesignUpdateView.as_view(), name='edit_design'),
    path('delete/<int:pk>/', views.DesignDeleteView.as_view(), name='delete_design'),
]

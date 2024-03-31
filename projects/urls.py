from django.urls import path
from . import views

urlpatterns = [
    path(
        'project-gallery/', views.ProjectGallery.as_view(),
        name='project_gallery'
        ),
    path(
        'project-gallery/add/', views.AddProjectImage.as_view(),
        name='add_project_image'
        ),
    path(
        'project-gallery/edit/<int:pk>/', views.EditProjectImage.as_view(),
        name='edit_project_image'
        ),
    path(
        'project-gallery/delete/<int:pk>/', views.DeleteProjectImage.as_view(),
        name='delete_project_image'
        ),
]
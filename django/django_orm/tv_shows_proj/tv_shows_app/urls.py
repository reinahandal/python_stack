from django.urls import path     
from . import views


urlpatterns = [
    path('shows/', views.index),
    path('shows/new/', views.add_show),
    path('shows/create/', views.create_show),
    path('shows/<show_id>/', views.read_show),
    path('shows/<show_id>/edit/', views.edit_show),
    path('shows/<show_id>/update/', views.update_show),
    path('shows/<show_id>/destroy/', views.delete_show),
]
from django.urls import path     
from . import views


urlpatterns = [
    path('shows/', views.index),
    path('shows/new/', views.add_show),
    path('shows/create/', views.create_show),
]
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.reset),
    path('gold/', views.index),
    path('process_money/', views.money)
]
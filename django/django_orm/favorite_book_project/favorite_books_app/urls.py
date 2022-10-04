from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('new/', views.add_book),
]
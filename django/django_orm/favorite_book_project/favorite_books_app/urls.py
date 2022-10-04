from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('new/', views.add_book),
    path('<int:book_id>/', views.show_book),
]
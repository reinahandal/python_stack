from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('new/', views.add_book),
    path('<book_id>/', views.show_book),
    path('<book_id>/update/', views.update_book),
    path('<book_id>/delete/', views.delete_book),
]
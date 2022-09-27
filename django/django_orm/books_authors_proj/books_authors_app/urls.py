from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_book),
    path('add_this_book/', views.add_this_book),
    path('books/<book_id>/', views.show_this_book),
    path('author_to_book/', views.author_to_book),
]
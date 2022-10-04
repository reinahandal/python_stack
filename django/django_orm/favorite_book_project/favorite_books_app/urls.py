from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('new/', views.add_book),
    path('<int:book_id>/', views.show_book),
    path('<int:book_id>/update/', views.update_book),
    path('<int:book_id>/delete/', views.delete_book),
    path('<int:book_id>/favorite/', views.favorite_book),
    path('<int:book_id>/unfavorite/', views.unfavorite_book),
    path('my_favorites/', views.my_favorites),
]
from django.db import models
from login_registration_app.models import User

class BookManager(models.Manager):
    def book_validator(self,postData):
        errors = {}
        if not postData['title']:
            errors['title'] = "Title is required"
        if len(postData['desc']) < 5:
            errors['desc'] = "Description should contain at least 5 characters"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_books", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()


def add_book(request):
    title = request.POST['title']
    desc = request.POST['desc']
    uploaded_by = User.objects.get(id=request.session['logged_user'])
    added_book = Book.objects.create(title=title, desc=desc,uploaded_by=uploaded_by)
    added_book.users_who_like.add(uploaded_by)


def update_book(request, book_id):
    book_to_update = Book.objects.get(id=book_id)
    book_to_update.title = request.POST['title']
    book_to_update.desc = request.POST['desc']
    book_to_update.save()


def delete_book(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()


def favorite_book(request, book_id):
    book_to_favorite = Book.objects.get(id=book_id)
    user_who_likes = User.objects.get(id=request.session['logged_user'])
    book_to_favorite.users_who_like.add(user_who_likes)


def unfavorite_book(request, book_id):
    book_to_unfavorite = Book.objects.get(id=book_id)
    user_who_dislikes = User.objects.get(id=request.session['logged_user'])
    book_to_unfavorite.users_who_like.remove(user_who_dislikes)
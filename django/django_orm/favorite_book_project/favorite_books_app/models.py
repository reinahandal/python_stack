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


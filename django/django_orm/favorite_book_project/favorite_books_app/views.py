from django.shortcuts import render, redirect
from . import models
from .models import User, Book
from django.contrib import messages

def books(request):
    if 'logged_user' in request.session:
        context = {
        "logged_user": User.objects.get(id=request.session['logged_user']),
        "first_name": User.objects.get(id=request.session['logged_user']).first_name,
        "all_books": Book.objects.all(),
        }
        return render(request, 'books_main.html', context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        models.add_book(request)
        return redirect('/books')


def show_book(request, book_id):
    if request.session['logged_user'] == Book.objects.get(id=book_id).uploaded_by.id:
        context = {
        "logged_user": User.objects.get(id=request.session['logged_user']),
        "first_name": User.objects.get(id=request.session['logged_user']).first_name,
        "book": Book.objects.get(id=book_id),
        }
        return render(request, 'update_book.html', context)
    else:
        context = {
        "logged_user": User.objects.get(id=request.session['logged_user']),
        "first_name": User.objects.get(id=request.session['logged_user']).first_name,
        "book": Book.objects.get(id=book_id),
        }
        return render(request, 'show_book.html', context)


def update_book(request, book_id):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/'+str(book_id))
    else:
        models.update_book(request, book_id)
        return redirect('/books/'+str(book_id))


def delete_book(request, book_id):
    models.delete_book(request, book_id)
    return redirect('/books/')


def favorite_book(request, book_id):
    models.favorite_book(request, book_id)
    return redirect('/books/'+str(book_id))


def unfavorite_book(request,book_id):
    models.unfavorite_book(request,book_id)
    return redirect('/books/'+str(book_id))


def my_favorites(request):
    logged_user = User.objects.get(id=request.session['logged_user'])
    context = {
        "first_name": User.objects.get(id=request.session['logged_user']).first_name,
        "my_favorites": logged_user.liked_books.all()
    }
    return render(request, 'my_favs.html', context)
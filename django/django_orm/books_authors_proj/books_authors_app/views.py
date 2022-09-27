from django.shortcuts import render, redirect
from .models import Book, Author

def add_book(request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }
    return render(request, 'add_book.html', context)


def add_this_book(request):
    title=request.POST['title']
    desc=request.POST['desc']
    Book.objects.create(title=title, desc=desc)
    return redirect('/')


def show_this_book(request, book_id):
    context = {
        "this_book": Book.objects.get(id=book_id),
        "all_authors": Author.objects.all(),
    }
    return render(request, 'show_book.html', context)


def author_to_book(request):
    author_to_add = Author.objects.get(id=request.POST['author_to_book'])
    target_book_id = request.POST['which_book']
    target_book = Book.objects.get(id=target_book_id)
    target_book.authors.add(author_to_add)
    return redirect('/books/'+target_book_id)


def add_author(request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }
    return render(request, 'add_author.html', context)


def add_this_author(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    notes=request.POST['notes']
    Author.objects.create(first_name=first_name, last_name=last_name,notes=notes)
    return redirect('/authors')


def show_this_author(request, author_id):
    context = {
        "this_author": Author.objects.get(id=author_id),
        "all_books": Book.objects.all(),
    }
    return render(request, 'show_author.html', context)


def book_to_author(request):
    book_to_add = Book.objects.get(id=request.POST['book_to_author'])
    target_author_id = request.POST['which_author']
    target_author = Author.objects.get(id=target_author_id)
    target_author.books.add(book_to_add)
    return redirect('/authors/'+target_author_id)

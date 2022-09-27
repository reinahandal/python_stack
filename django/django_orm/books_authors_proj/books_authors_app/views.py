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



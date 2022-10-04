from django.shortcuts import render, redirect
from . import models
# from .models import 

def books(request):
    if 'logged_user' in request.session:
        return render(request, 'books_main.html')

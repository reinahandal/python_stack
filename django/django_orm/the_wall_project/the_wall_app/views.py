from django.shortcuts import render, redirect
from . import models
from .models import Message
from django.contrib import messages

def display_wall(request):
    if 'user_first_name' in request.session:
        context = {
            "messages": Message.objects.all().order_by("-created_at")
        }
        return render(request, 'wall.html', context)
    else:
        return redirect('/')

def post_message(request):
    models.post_message(request)
    return redirect('/wall')

def add_comment(request):
    models.add_comment(request)
    return redirect('/wall')

def delete_message(request):
    models.delete_message(request)
    return redirect('/wall')

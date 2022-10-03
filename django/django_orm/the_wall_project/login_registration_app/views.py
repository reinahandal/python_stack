from django.shortcuts import render, redirect
from .models import User
from . import models


def index(request):
    return render(request, 'index.html')

# This method executes the registration method if no errors were found in validation
def registration(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        models.registration(request)
        return redirect('/wall')

#This method checks if user email exists in DB (i.e if user is registered)
def login(request):
    try:
        logged_user = User.objects.get(email=request.POST['login_email'])
    except:
        return redirect('/')
    else:
        if models.is_authenticated(request, logged_user):
            request.session['user_first_name'] = logged_user.first_name
            return redirect('/wall')


def logout(request):
    del request.session['user_first_name']
    return redirect('/')
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        birthday = request.POST['birthday']
        password = request.POST['pw']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() # hashes the entered password
        User.objects.create(first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=pw_hash)
        request.session['logged_user'] = first_name # creates session
        return redirect('/success')


def login(request):
    # user = User.objects.filter(email=request.POST['login_email']) # checks if user email exists in DB, returns arr
    # if user:
    #     logged_user = user[0] # considering we have unique emails due to validation
    #     if bcrypt.checkpw(request.POST['login_pw'].encode(), logged_user.password.encode()): # checks that login pw matches one in DB after hashing
    #         request.session['logged_user'] = logged_user.first_name #creates session
    #         return redirect('/success')
    # return redirect('/') # if user doesnt exist, redirect to root route
    try:
        logged_user = User.objects.get(email=request.POST['login_email'])
    except:
        return redirect('/')
    else:
        if bcrypt.checkpw(request.POST['login_pw'].encode(), logged_user.password.encode()):
            request.session['logged_user'] = logged_user.first_name
            return redirect('/success')


def success(request):
    if 'logged_user' in request.session: # doesnt allow user that isnt logged in to access this page 
        return render(request, 'success.html')
    else:
        return redirect('/')

def logout(request):
    del request.session['logged_user']
    return redirect('/')
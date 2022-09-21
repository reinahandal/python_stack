from django.shortcuts import render, redirect
import random

def index(request):
    return render(request,'index.html')
def money(request):
    if request.POST['activity'] == 'farm' or request.POST['activity'] == 'cave' or request.POST['activity'] == 'house':
        random_number = random.randint(10, 20)
        request.session['random_number'] = random_number
    elif request.POST['activity'] == 'quest':
        random_number = random.randint(-50, 50)
        request.session['random_number'] = random_number
    request.session['gold_counter'] += random_number
    return redirect('/gold/')
def reset(request):
    request.session['gold_counter'] = 0
    return redirect('gold/')
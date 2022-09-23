from django.shortcuts import render, redirect
import random
from time import strftime, localtime

def index(request):
    return render(request,'index.html')

def money(request):
    time = strftime("%b %d, %Y, %H:%M %p", localtime())
    if request.POST['activity'] == 'farm' or request.POST['activity'] == 'cave' or request.POST['activity'] == 'house':
        random_number = random.randint(10, 20)
        current_activity = request.POST['activity']
        request.session['random_number'] = random_number
        request.session['current_activity'] = current_activity
        request.session['activity_log'].insert(0, ['You entered a '+ current_activity + ' and earned ' + str(random_number) + ' gold. (' + time + ')', 'success'])

    elif request.POST['activity'] == 'quest':
        random_number = random.randint(-50, 50)
        current_activity = request.POST['activity']
        request.session['random_number'] = random_number
        request.session['current_activity'] = current_activity
        if random_number < 0:
            request.session['activity_log'].insert(0, ['You failed a quest and lost ' + str(random_number) + ' gold. Ouch. (' + time + ')', 'lose'])
        else:
            request.session['activity_log'].insert(0, ['You entered a quest and earned ' + str(random_number) + ' gold. (' + time + ')', 'success'])
    print(random_number)
    request.session['gold_counter'] += random_number
    return redirect('/gold/')

def reset(request):
    request.session['gold_counter'] = 0
    request.session['activity_log'] = []
    if "current_activity" in request.session:
        del request.session['current_activity']
    return redirect('gold/')
from django.shortcuts import render, redirect
import random
from time import strftime, localtime

def index(request):
    if 'gold_counter' and 'activity_log' not in request.session:
        request.session['gold_counter'] = 0
        request.session['activity_log'] = []
    return render(request,'index.html')

def money(request):
    time = strftime("%b %d, %Y, %H:%M %p", localtime())
    random_number = random.randint(-50, 50) if request.POST['activity'] == 'quest' else random.randint(10, 20)
    if request.POST['activity'] == 'farm' or request.POST['activity'] == 'cave' or request.POST['activity'] == 'house':
        current_activity = request.POST['activity']
        request.session['current_activity'] = current_activity
        request.session['activity_log'].insert(0, ['You entered a '+ current_activity + ' and earned ' + str(random_number) + ' gold. (' + time + ')', 'success'])

    elif request.POST['activity'] == 'quest':
        current_activity = request.POST['activity']
        request.session['current_activity'] = current_activity
        if random_number < 0:
            random_number = random_number * -1
            request.session['activity_log'].insert(0, ['You failed a quest and lost ' + str(random_number) + ' gold. Ouch. (' + time + ')', 'lose'])
        else:
            request.session['activity_log'].insert(0, ['You entered a quest and earned ' + str(random_number) + ' gold. (' + time + ')', 'success'])
    print(random_number)
    request.session['gold_counter'] += random_number
    return redirect('/gold/')

def reset(request):
    if "current_activity" in request.session:
        del request.session['current_activity']
        del request.session['gold_counter']
        del request.session['activity_log']
    return redirect('gold/')
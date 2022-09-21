from django.shortcuts import render, redirect

def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1
    print('this is counter 1: ' + str(counter))
    return render(request, 'index.html')
def destroy(request):
    del request.session['counter']
    # del request.session['temp']
    return redirect('/')
def add_two(request):
    counter2 = request.session.get('counter', 0)
    request.session['counter'] = counter2 + 1
    print('this is counter 2: ' + str(counter2)) 
    # temp = request.session.get('temp', 2)
    # request.session['temp'] = temp + 2
    # print('this is temp: ' + str(temp)) 
    return redirect('/')
def custom_number(request):
    counter3 = request.session.get('counter', 0)
    custom_number = int(request.POST['custom_number'])
    request.session['counter'] = counter3 + custom_number  - 1
    return redirect('/')

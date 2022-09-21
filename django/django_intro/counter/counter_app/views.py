from django.shortcuts import render, redirect

def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1
    return render(request, 'index.html')
def destroy(request):
    del request.session['counter']
    return redirect('/')
def add_two(request):
    counter2 = request.session.get('counter', 0)
    request.session['counter'] = counter2 + 1
    return redirect('/')
def custom_number(request):
    counter3 = request.session.get('counter', 0)
    custom_number = int(request.POST['custom_number'])
    request.session['counter'] = counter3 + custom_number  - 1
    return redirect('/')

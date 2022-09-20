from django.shortcuts import render

def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1
    return render(request, 'index.html')
def destroy(request):
    del request.session['counter']
    return render(request,'index.html')

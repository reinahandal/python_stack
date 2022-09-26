from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "all_dojos": Dojo.objects.all(),
        "all_ninjas": Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def new_dojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(name=name, city=city, state=state)
    return redirect('/')


def new_ninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/')


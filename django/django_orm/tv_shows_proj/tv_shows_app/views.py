from django.shortcuts import render, redirect
from .models import Show

def index(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'index.html', context)

def add_show(request):
    return render(request, 'create.html')


def create_show(request):
    title=request.POST['title']
    network=request.POST['network']
    release_date=request.POST['release_date']
    desc=request.POST['desc']
    Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
    return redirect('/shows')
    # must redirect to /shows/<id>

from django.shortcuts import render, redirect
from .models import Show
from time import strftime
from django.contrib import messages


def root(request):
    return redirect('/shows')


def index(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'index.html', context)

def add_show(request):
    return render(request, 'create.html')


def create_show(request):
    title_error = Show.objects.title_validator(request.POST)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0 or len(title_error) > 0:
        for key, value in title_error.items():
            messages.error(request, value)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
        
    else:
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['release_date']
        desc=request.POST['desc']
        new_show = Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
        show_id = new_show.id

        return redirect('/shows/'+str(show_id)+'/')



def read_show(request, show_id):
    context = {
        "tv_show": Show.objects.get(id=show_id),
    }
    return render(request, 'read.html', context)


def edit_show(request, show_id):
    context = {
        "tv_show": Show.objects.get(id=show_id),
        "tv_show_release_date": Show.objects.get(id=show_id).release_date.strftime('%Y-%m-%d')
    }
    return render(request, 'update.html', context)


def update_show(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+show_id+'/edit')
    else:
        new_title=request.POST['title']
        new_network=request.POST['network']
        new_date=request.POST['release_date']
        new_desc=request.POST['desc']
        show_to_update = Show.objects.get(id=show_id)
        show_to_update.title = new_title
        show_to_update.network = new_network
        show_to_update.release_date = new_date
        show_to_update.desc = new_desc
        show_to_update.save()

        return redirect('/shows/'+show_id)

def delete_show(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')

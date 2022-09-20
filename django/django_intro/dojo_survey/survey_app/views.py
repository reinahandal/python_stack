from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def show(request):
    context = {
    'name': request.POST['name'],
    'location': request.POST['location'],
    'language': request.POST['language'],
    'background': request.POST['background'],
    'comment': request.POST['comment'],
    'career_service': request.POST['career-service'],
    'newsletter': request.POST['newsletter'],
    'challenges': request.POST['challenges'],
    }
    return render(request, "show.html", context)
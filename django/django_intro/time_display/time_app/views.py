from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%H:%M %p", localtime())
    }
    return render(request, 'index.html', context)
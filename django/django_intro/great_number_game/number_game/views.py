from django.shortcuts import render, redirect, HttpResponse
def index(request):
    import random
    if "random_number" not in request.session:
        random_number = random.randint(1, 100)
        request.session['random_number'] = random_number
    # print(random_number)
    return render(request,'index.html')
def submit_guess(request):
    random_guess = int(request.POST['random_guess'])
    # print(random_guess)
    print(request.session['random_number'])
    if random_guess > request.session['random_number']:
        request.session['user_guess'] = "too_high"
    elif random_guess < request.session['random_number']:
        request.session['user_guess'] = "too_low"
    elif random_guess == request.session['random_number']:
        request.session['user_guess'] = "correct"
    return redirect('/')
def play_again(request):
    del request.session['random_number']
    del request.session['user_guess']
    return redirect('/')
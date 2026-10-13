from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    context = {
        'result': request.session.get('result'),
        'won': request.session.get('won'),
    }
    return render(request, 'index.html', context)

def guess(request):
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        number = request.session['number']
        if guess < number:
            request.session['result'] = 'Too low!'
        elif guess > number:
            request.session['result'] = 'Too high!'
        else:
            request.session['result'] = f'{number} was the number!'
            request.session['won'] = True
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
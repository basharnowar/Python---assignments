from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
     if 'gold' not in request.session:
        request.session['gold'] = 0
        
     return render(request, "index.html" )

        

def process(request):
    building = request.POST['building']
    if building == 'farm':
        amount = random.randint(10, 20)
    elif building == 'cave':
        amount = random.randint(5, 10)
    elif building == 'house':
        amount = random.randint(2, 5)
    elif building == 'casino':
        amount = random.randint(-50, 50)
    request.session['gold'] += amount
    return redirect('/')
    
    
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt 

# Create your views here.
def index(request):
    return redirect('/register')


def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')

        password = request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=request.POST['first_name'], 
                                   last_name=request.POST['last_name']
                                   ,email=request.POST['email'], 
                                   password=hashed_password)
        return redirect(f'/success/{user.id}')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        users = User.objects.filter(email=request.POST['email'])

        if users:
           logged_user = users[0]
           
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
         return redirect(f'/success/{ logged_user.id }')

        messages.error(request, "Invalid Email/Password")
        
    return render(request, 'register.html')


def success(request, id):
    context = {
        'user' : User.objects.get(id=id)
    }
    return render(request, 'success.html', context)



         
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .models import UserManager
from django.contrib import messages
import bcrypt

# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def create_user(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register/')

        password = request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_password
        )
        request.session['user_id'] = new_user.id
        return redirect('/wall/')
    return redirect('/register/')



def check_login(request):
    if request.method == 'POST':
        users = User.objects.filter(email=request.POST['email'])
        if users:
            logged_user = users[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/wall/')
        messages.error(request, "Invalid Email or Password")
        return redirect('/login/')
    return redirect('/login/')




def logout(request):
    request.session.clear()
    return redirect('/login/')



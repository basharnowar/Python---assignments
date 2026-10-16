from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    Dojos = Dojo.objects.all()

    context = {
        "dojos" : Dojos 
    }
    return render(request, "index.html", context)

def create_dojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        Dojo.objects.create(name=name, city=city, state=state)
        return redirect('/')
    return redirect('/')

def create_ninja(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo = Dojo.objects.get(id=request.POST['dojo_id'])
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
        return redirect('/')
    return redirect('/')


def delete(request, id):

    my_del = Dojo.objects.get(id=id)
    my_del.delete()

    return redirect('/')



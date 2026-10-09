from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    return HttpResponse("Place holder to display a list of all blogs")

def new(request):
    return HttpResponse("Place holder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def numbers(request, number):
    return HttpResponse(f"Place holder to display blog number: {number}")

def nums(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redirect('/blogs/')


def root(request):
    return redirect('/blogs/')






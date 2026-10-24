from django.shortcuts import render, HttpResponse, redirect
from loginapp.models import User
from .models import Message, Comment
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

# Create your views here.

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    context = {
        "logged_user": User.objects.get(id=request.session['user_id']),
        "all_messages": Message.objects.all().order_by("-created_at")
    }
    return render(request, "wall.html", context)

def post_message(request):
    if request.method == 'POST':
        Message.objects.create(
            message=request.POST['message'],
            User=User.objects.get(id=request.session['user_id'])
        )
        return redirect('/wall/')
    return redirect('/wall/')


def post_comment(request):
    if request.method == 'POST':
        Comment.objects.create(
            comment=request.POST['comment'],
            User=User.objects.get(id=request.session['user_id']),
            Message=Message.objects.get(id=request.POST['message_id'])
        )
        return redirect('/wall/')
    return redirect('/wall/')

def delete_message(request):
    if request.method == 'POST':
        message = Message.objects.get(id=request.POST['message_id'])
        if message.User.id == request.session['user_id']:
            if timezone.now() - message.created_at < timedelta(minutes=30):
                message.delete()
            else:
                messages.error(request, "You can only delete a message within 30 minutes of posting it")
        return redirect('/wall/')
    return redirect('/wall/')

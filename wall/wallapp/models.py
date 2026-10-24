from django.db import models
from loginapp.models import User

# Create your models here.


class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    Message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comments")


    




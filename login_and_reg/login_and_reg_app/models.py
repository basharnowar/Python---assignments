from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        
        if len(postData['email']) < 3:
            errors['email'] = "email should be 3 characters"

        if len(postData['password']) < 2:
            errors['password'] = "passoword must be 2 characters"

        return errors




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    objects = UserManager()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

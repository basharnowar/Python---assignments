from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, PostData):
        errors = {}

        if len(PostData['first_name']) < 2:
           errors['first_name'] = "First name should be at least 2 characters"

        if len(PostData['last_name']) < 2:
           errors['last_name'] = "Last name should be at least 2 characters"

        if len(PostData['email']) < 5:
           errors['email'] = "Email must have at least 5 characters"

        if len(PostData['password']) < 8:
           errors['password'] = "Password must have at least 8 characters"

        if PostData['password'] != PostData['confirm_password']:
           errors['confirm_password'] = "Passwords do not match"

        if len(User.objects.filter(email=PostData['email'])) > 0:
           errors['email_taken'] = "This email already taken"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



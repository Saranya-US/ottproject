from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # You should use a more secure way to store passwords
    DoB = models.DateField()
    phonenumber = models.CharField(max_length=15)

    # Provide unique related_names for the groups and user_permissions fields
    # groups = models.ManyToManyField(Group, related_name='customer_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='customer_user_permissions')



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='profile_images/')
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models


class customer(models.Model):
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

    def __str__(self):
        return self.firstname

from datetime import date

from django.contrib.auth.hashers import make_password,check_password
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
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, limit_choices_to={'profile__isnull': True})
    name = models.CharField(max_length=255)


class UserProfile(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')
    pin = models.CharField(max_length=6, null=True, blank=True)  # Hashed PIN
    dob = models.DateField(null=True, blank=True)

    # Date of Birth
    def is_kid(self):
        # Add your logic to determine if the user is a kid (e.g., age check)
        # Return True if it's a kid, False otherwise
        return True if self.calculate_age() < 18 else False
    def set_pin(self, raw_pin):
        self.pin = make_password(raw_pin)

    def check_pin(self, raw_pin):
        return check_password(raw_pin, self.pin) if self.pin else False

    def calculate_age(self):
        if self.dob:
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return None

    def __str__(self):
        return self.name

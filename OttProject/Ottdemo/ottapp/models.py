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

    def set_pin(self, raw_pin):
        self.pin = make_password(raw_pin)

    def check_pin(self, raw_pin):
        return check_password(raw_pin, self.pin) if self.pin else False

    def __str__(self):
        return self.name


class KidsProfile(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')

class Adult_Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    language = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    ratings = models.FloatField(default=0.0)  # Ratings on a scale from 0 to 5
    image = models.ImageField(upload_to='movie_image/')
    video = models.FileField(upload_to='movie_videos/')


class Kids_Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    language = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    ratings = models.FloatField(default=0.0)  # Ratings on a scale from 0 to 5
    image = models.ImageField(upload_to='movie_image/')
    video = models.FileField(upload_to='movie_videos/')

class Adult_WatchHistory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Adult_Movie, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Adult_WatchLater(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Adult_Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

class Adult_Suggestions(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    suggested_movie = models.ForeignKey(Adult_Movie, on_delete=models.CASCADE)


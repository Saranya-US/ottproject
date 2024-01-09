from django.contrib import admin
from .models import Customer, UserProfile


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname','username', 'password', 'email','phonenumber') # Customize the fields you want to display

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('name','image')
#


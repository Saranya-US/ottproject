# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Customer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'email', 'username', 'password', 'DoB', 'phonenumber']
        widgets = {
            'password1': forms.PasswordInput(),
        }



class ProfileForm(forms.Form):
    name = forms.CharField(max_length=255)

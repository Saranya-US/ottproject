# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.html import format_html

from .models import Customer, UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'email', 'username', 'password', 'DoB', 'phonenumber']
        widgets = {
            'password1': forms.PasswordInput(),
            'DoB': forms.DateInput(attrs={'type': 'date'}),
        }


class VerifyPinForm(forms.Form):
    pin = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': 6}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'image', 'pin', 'dob']


# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None  # Remove username guidelines
        self.fields['password'].help_text = None  # Remove password guidelines


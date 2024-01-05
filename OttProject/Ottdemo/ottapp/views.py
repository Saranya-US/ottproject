from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm
from .models import customer  # Corrected model name to follow PEP8 conventions

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

def registration_view(request):
    if request.method == 'POST':
        # Process the form data (handle registration logic here)
        pass
    else:
        # Display the registration form
        return render(request, 'register_form.html')


def home(request):
    return render(request,'home.html')


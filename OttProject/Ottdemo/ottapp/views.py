from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from .models import customer  # Corrected model name to follow PEP8 conventions

def login_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a user profile
            customer.objects.create(user=user)

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, template_name='login.html', context={'form': form})


def home(request):
    return render(request,'home.html')
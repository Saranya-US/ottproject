from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,authenticate
from .forms import LoginForm, CustomerRegistrationForm,UserProfileForm
from .models import Customer,UserProfile  # Corrected model name to follow PEP8 conventions
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                customer = Customer.objects.get(username=username)
                if customer.password == password:
                    return render(request, 'profiles/profile_selection.html')
                else:
                    form.add_error(None, 'Invalid credentials')
            except Customer.DoesNotExist:
                form.add_error(None, 'User not found')

    return render(request, 'registration/login.html',{'form':form})

def register_view(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = CustomerRegistrationForm()

    return render(request, 'register_form.html', {'form': form})


def home(request):
    return render(request,'home.html')


def profile_selection(request):
    profiles = UserProfile.objects.filter(user=request.user)
    return render(request, 'profiles/profile_selection.html', {'profiles': profiles})


@login_required
def add_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.customer = request.user
            profile.save()
            messages.success(request, 'Profile added successfully.')
            return redirect('profile_selection')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = UserProfileForm()

    return render(request, 'profiles/add_profile.html', {'form': form})



def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profiles/profile.html', {'user_profile': user_profile})


def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})

# views.py



def view_profile(request, user_id):
    userprofile = get_object_or_404(UserProfile, user_id=user_id)
    return render(request, 'profiles/view_profile.html', {'userprofile': userprofile})


def profile_list(request):
    profiles = UserProfile.objects.all()  # Assuming 'created_at' is a DateTimeField in your model
    return render(request, 'profiles/profile_selection.html', {'profiles': profiles })
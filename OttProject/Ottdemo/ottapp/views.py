from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import LoginForm, CustomerRegistrationForm, ProfileForm
from .models import Customer, Profile, UserProfile  # Corrected model name to follow PEP8 conventions

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
                    return render(request, 'profiles/add_profile.html')
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
    profiles = Profile.objects.filter(user=request.user)
    return render(request, 'profiles/profile_selection.html', {'profiles': profiles})

def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_selection')
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile_selection.html', {'form': form})

def profile_list(request):
    profiles = UserProfile.objects.all()
    print("list")
    return render(request, 'welcome.html', {'profiles': profiles})


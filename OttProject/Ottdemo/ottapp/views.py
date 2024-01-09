from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,authenticate
from .forms import LoginForm, CustomerRegistrationForm, ProfileForm, VerifyPinForm
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
                    customer_id = customer.id
                    return redirect( 'profile_selection',customer_id = customer_id)
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


def profile_selection(request,customer_id):
    customer=Customer.objects.get(id=customer_id)
    profiles = UserProfile.objects.all()  # Fetch all profiles
    return render(request, 'profiles/profile_selection.html', {'customer':customer,'profiles': profiles})



def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'welcome.html', {'profiles': profiles})

def verify_pin(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id)

    if request.method == 'POST':
        form = VerifyPinForm(request.POST)
        if form.is_valid() and profile.check_pin(form.cleaned_data['pin']):
            return redirect('welcome')  # Redirect to the welcome page upon successful PIN verification
        else:
            form.add_error('pin', 'Invalid PIN')
    else:
        form = VerifyPinForm()

    return render(request, 'profiles/verify_pin.html', {'form': form, 'profile': profile})


def add_profile(request, customer_id):
    template_name = 'profiles/add_profile.html'
    customer = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            customer = get_object_or_404(Customer, id=customer_id)

            # Create a UserProfile instance but don't save it yet
            profile = form.save(commit=False)

            # Associate the profile with the customer
            profile.user = customer

            # Optionally set the PIN using the set_pin method in UserProfile model
            # profile.set_pin(form.cleaned_data['pin'])

            # Save the profile to the database
            profile.save()

            # Redirect to a success page or any other desired page
            return redirect('profile_selection', customer_id=customer.id)
        else:
            form.add_error('image', 'Invalid avatar choice')  # Handle invalid choice
    else:
        form = ProfileForm()

    return render(request, template_name, {'customer': customer, 'form': form})


def store_profile_details(request, customer_id):
    customer = Customer.objects.get(id=customer_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a UserProfile instance but don't save it yet
            profile = form.save(commit=False)

            # Associate the profile with the customer
            profile.customer = customer

            # Save the profile to the database
            profile.save()

            # Redirect to a success page or any other desired page
            return redirect('profile_selection', customer_id=customer.id)
        else:
            form.add_error('image', 'Invalid avatar choice')  # Handle invalid choice
    else:
        form = ProfileForm()

    return render(request, 'add_profile.html', {'customer': customer, 'form': form})
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,authenticate
from .forms import LoginForm, CustomerRegistrationForm, ProfileForm, VerifyPinForm, KidProfileForm
from .models import Customer, Profile, UserProfile, KidsProfile  # Corrected model name to follow PEP8 conventions
from django.views.generic import TemplateView


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

def welcome(request):
    return render(request, 'welcome.html')


# views.py
def profile_selection(request, customer_id):
    customer = Customer.objects.get(id=customer_id)

    # Fetch adult profiles
    adult_profiles = UserProfile.objects.filter(user=customer)

    # Fetch kids' profiles
    kids_profiles = KidsProfile.objects.filter(user=customer)

    return render(request, 'profiles/profile_selection.html', {
        'customer': customer,
        'adult_profiles': adult_profiles,
        'kids_profiles': kids_profiles,
    })




def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'welcome.html', {'profiles': profiles})

import hmac

def verify_pin(request, user_profile_id):
    template_name = 'profiles/verify_pin.html'

    user_profile = get_object_or_404(UserProfile, id=user_profile_id)

    if request.method == 'POST':
        form = VerifyPinForm(request.POST)
        if form.is_valid():
            provided_pin = form.cleaned_data['pin']
            stored_pin = user_profile.pin

            # Use constant-time comparison to mitigate timing attacks
            if hmac.compare_digest(provided_pin, stored_pin):
                print("PIN is correct. Redirecting to welcome page.")
                return redirect('welcome')
            else:
                form.add_error('pin', 'Invalid PIN')
                print(f'Invalid PIN: {form.errors}')
        else:
            print(f'Invalid form: {form.errors}')
    else:
        form = VerifyPinForm()

    return render(request, template_name, {'form': form, 'user_profile': user_profile})


class ErrorPageView(TemplateView):
    template_name = 'profiles/error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_message'] = "You can create a maximum of 4 profiles only."
        return context

# Your existing imports and views

def add_profile(request, customer_id):
    template_name = 'profiles/add_profile.html'

    customer = get_object_or_404(Customer, id=customer_id)

    # Check the number of existing profiles for the customer
    existing_profiles_count = UserProfile.objects.filter(user=customer).count()

    # Check if the limit has been reached
    limit_reached = existing_profiles_count >= 4

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and not limit_reached:
            # Create a UserProfile instance but don't save it yet
            profile = form.save(commit=False)

            # Associate the profile with the customer
            profile.user = customer

            # Save the profile to the database
            profile.save()

            # Fetch the list of profiles again
            profiles = UserProfile.objects.filter(user=customer)

            # Redirect to a success page or any other desired page
            return redirect('profile_selection', customer_id=customer.id)
        else:
            form.add_error('image', 'Invalid avatar choice')  # Handle invalid choice

    else:
        form = ProfileForm()

    if limit_reached:
        error_message = "You can create a maximum of 4 profiles only."
        return render(request, 'profiles/error.html', {'error_message': error_message})

    return render(request, template_name, {'form': form, 'limit_reached': limit_reached})

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

# views.py
# views.py
def register_kid_profile(request, customer_id):
    template_name = 'profiles/add_kids_profile.html'

    customer = Customer.objects.get(id=customer_id)

    # Check if the limit for kid profiles has been reached
    kid_profiles_limit = 2  # Set the desired limit for kid profiles
    kid_profiles_count = KidsProfile.objects.filter(user=customer).count()

    if kid_profiles_count >= kid_profiles_limit:
        error_message = f"You can create a maximum of {kid_profiles_limit} kid profiles only."
        return render(request, 'profiles/error.html', {'error_message': error_message})

    if request.method == 'POST':
        form = KidProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a KidsProfile instance but don't save it yet
            kid_profile = form.save(commit=False)

            # Associate the kid profile with the customer
            kid_profile.user = customer

            # Save the kid profile to the database
            kid_profile.save()

            # Redirect to a success page or any other desired page
            return redirect('profile_selection', customer_id=customer.id)
        else:
            form.add_error('image', 'Invalid avatar choice')  # Handle invalid choice
    else:
        form = KidProfileForm()

    return render(request, template_name, {'customer': customer, 'form': form})


from django.urls import path
from .views import home, login_view, register_view, add_profile, profile_selection

urlpatterns = [
    path('', home, name='home'),  # Updated URL pattern to include 'signup/'
    path('login/',login_view, name='login'),
    path('register_form/', register_view, name='register_form'),
    path('profile_selection/', profile_selection, name='profile_selection'),
    path('add_profile/', add_profile, name='add_profile'),
]



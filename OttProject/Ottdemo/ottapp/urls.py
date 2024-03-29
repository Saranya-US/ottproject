

from django.urls import path
from .views import home, login_view, register_view, add_profile, profile_selection, profile_list, verify_pin, \
    store_profile_details, ErrorPageView, register_kid_profile, welcome

urlpatterns = [
    path('', home, name='home'),  # Updated URL pattern to include 'signup/'
    path('login/',login_view, name='login'),
    path('register_form/', register_view, name='register_form'),
    path('profile_selection/<int:customer_id>/', profile_selection, name='profile_selection'),
    path('add_profile/<int:customer_id>/', add_profile, name='add_profile'),
    path('add_kids_profile/<int:customer_id>/', register_kid_profile, name='add_kids_profile'),
    path('profiles/', profile_list, name='profile_list'),
    path('verify_pin/<int:user_profile_id>/', verify_pin, name='verify_pin'),
    path('store_profile_details/<int:customer_id>/', store_profile_details, name='store_profile_details'),
    path('error/', ErrorPageView.as_view(), name='error_page'),
    path('welcome/', welcome, name='welcome'),

]


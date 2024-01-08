
from django.urls import path
from .views import home, login_view, register_view, add_profile, edit_profile, view_profile, profile, \
     profile_list

urlpatterns = [
    path('', home, name='home'),  # Updated URL pattern to include 'signup/'
    path('login/',login_view, name='login'),
    path('register_form/', register_view, name='register_form'),
    path('profile_selection/',profile_list, name='profile_selection'),
    path('profiles/add_profile/', add_profile, name='add_profile'),
    path('userprofile/',profile,name='userprofile'),
    path('profiles/edit/', edit_profile, name='edit_profile'),
    path('profile/<int:user_id>/', view_profile, name='view_profile'),

]



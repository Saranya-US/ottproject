
from django.urls import path
from .views import home, login_user

urlpatterns = [
    path('', home, name='home'),  # Updated URL pattern to include 'signup/'
    path('login/', login_user, name='login'),  # Updated to use login_user
]

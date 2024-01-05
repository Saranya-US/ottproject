
from django.urls import path
from .views import home, CustomLoginView, registration_view

urlpatterns = [
    path('', home, name='home'),  # Updated URL pattern to include 'signup/'
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register_form/', registration_view, name='register_form')
]

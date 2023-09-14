from django.urls import path
from .views import dashboard, Profile, register

app_name = 'profiles'
urlpatterns =[ path('', dashboard, name='dashboard'),
              path('profile/<pk>', Profile.as_view(), name='profile'),
              path('register/', register, name='register')]
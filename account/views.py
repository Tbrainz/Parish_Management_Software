from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .forms import LoginForm
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
           username = request.POST['username'] 
           password = request.POST['password']

           user = authenticate(request, username = username, password = password)
           if user:
               login(request, user)
               messages.success(request, 'You are logged in ')
               return redirect('profiles:dashboard')
           else:
                messages.error(request, 'please try again')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'login_form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('core:home')


def password_reset(request):
    return render(request, 'password_reset.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AnnouncementModel, MassBookingModel
from .forms import AnnouncementForm, MassBookingForm, RegistrationForm
from account.models import ProfileModel
from account.forms import ProfileForm
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib import messages
# Create your views here.
@login_required(login_url='account:login')
def dashboard(request):
    annForm = AnnouncementForm()
    annModel = AnnouncementModel.objects.all()
    proModel = ProfileModel.objects.all()
    massBook = MassBookingForm()

    if request.method == 'POST':
        massBook = MassBookingForm(request.POST)
        if massBook.is_valid():
            massBook.save()
            messages.success(request, 'Your Mass Intention has been booked Successfully')
            return redirect('profiles:dashboard')
        else:
            messages.error(request, 'There was an error, please try again')
            messages.error(request, massBook.errors)
    if request.method == 'POST':
        annForm = AnnouncementForm(request.POST)
        if annForm.is_valid():
            annForm.save()
            messages.success(request, 'Announcement Submitted Successfully.')
            return redirect('profiles:dashboard')
        else:
            messages.error(request, 'There was an error, please try again')
            messages.error(request, annForm.errors)


    return render(request, 'dashboard.html', 
                  {'profiles':proModel, 'annForm': annForm, 'annModel':annModel, 'massBook': massBook})

class Profile(UpdateView):
    template_name = 'profile.html'
    form_class = ProfileForm
    model = ProfileModel
    success_message = 'Profile updated successfully'
    success_url = 'profiles:dashboard'


@login_required(login_url='account:login')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, 'Registration Successful')
               return redirect('account:login')
          messages.error(request, 'Unsuccessful, Try again')
    return render(request, 'register.html', {'form':form})
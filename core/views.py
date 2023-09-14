from django.shortcuts import render, redirect
from account.forms import ContactForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'index.html')


def ppc(request):
    return render(request, 'ppc.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was submited')
            return redirect('core:contact')
    
    return render(request, 'contact.html', {'form':form})
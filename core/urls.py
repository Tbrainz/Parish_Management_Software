from django.urls import path
from .views import (home, ppc, about, gallery, events, contact,)

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('ppc/', ppc, name='ppc'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('events/', events, name='events'),
    path('contact/', contact, name='contact'),
]
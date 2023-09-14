from django.forms import ModelForm, TextInput, EmailInput,Textarea, DateInput, PasswordInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AnnouncementModel, MassBookingModel

class RegistrationForm(UserCreationForm):

    class Meta:
         model = User
         fields = ("username", "email", "password1", "password2")

         
        #  widgets = {
        #         'username': TextInput(attrs={
        #             'class': "form-control",
        #             'style': 'width: 500px; margin:10px 0;',
                    
        #             }),
        #         'email': EmailInput(attrs={
        #             'class': "form-control",
        #             'style': 'width: 500px; margin:10px 0;',
                    
        #             }),
        #         'password1': PasswordInput(attrs={
        #             'class': "form-control",
        #             'style': 'width: 500px; margin:10px 0;',
                    
        #             }),
        #         'password2': PasswordInput(attrs={
        #             'class': "form-control",
        #             'style': 'width: 500px; margin:10px 0;',
                    
        #             }),
        #     }
         label ={'username':'User Name', 'email':'Email', 'password1':'Password', 'password2':'Confirm Password'}

       
         
class AnnouncementForm(ModelForm):
    class Meta:
        model = AnnouncementModel
        fields = '__all__'


        widgets = {
            'organization': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 500px; margin:10px 0;',
                'placeholder': 'Organization'
                }),
            'date': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Date'
                }),

            'announcement': Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),

            'marital_status': Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),

             'marital_status': Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),
        }


class MassBookingForm(ModelForm):
    class Meta:
        model = MassBookingModel
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 500px; margin:10px 0;',
                
                'placeholder': 'Name'
                }),
            'number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Number'
                }),

            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Email'
                }),

            'thanksgiving':forms.Select (
                choices=[('YES', 'YES'), ('NO', 'NO')],
                attrs={
                    'class':'bootstrap-select',
                    'style' : 'max-width: 500px; margin:10px 0;'
                }
            ),

            'intention': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Intention'
                }),
        }
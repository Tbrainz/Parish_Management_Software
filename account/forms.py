from django import forms
from django.forms import ModelForm, TextInput,PasswordInput ,EmailInput,Textarea, DateInput, FileInput, DateTimeInput
from .models import ProfileModel
from profiles.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
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

            'email': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'email'
                }),

            'message': Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Message'
                }),
        }

        label = {'name':'Full Name', 'number':'Number', 'email':'Email', 'message':'Message'}

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'   
       
class LoginForm(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300)
 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
       

        
        widgets = {
            'full_name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 500px; margin:10px 0;',
                'placeholder': 'Organization'
                }),
            'number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Date'
                }),

            'address': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),

            'marital_status':forms.Select (
                choices=[('Single', 'Single'), ('Married', 'Married')],
                attrs={
                    'class':'bootstrap-select',
                    'style' : 'max-width: 500px; margin:10px 0; margin-left:10px;'
                }
            ),

            'tribe': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),
            
            'occupation': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),

            'societies': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),

            'dob': DateTimeInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),

            'image': FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px; margin:10px 0;',
                'placeholder': 'Announcement'
                }),
        }
        label = {'full_name':'Full Name', 'number': 'Number', 'address': 'Address',
                'marital_status': 'Marital Status', 'tribe': 'Tribe',
                 'occupation': 'Occupation', 'societies':'Societies', 
                 'dob':'Date of Birth', 'image':'Profile Picture'}  
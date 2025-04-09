from django import forms
from django.contrib.auth import models
from django.forms import ModelForm, fields
from .models import user_registration



class usersform(ModelForm):
    class Meta:
        model = user_registration
        fields = ('event_name','first_name', 'last_name', 'email', 'block', 'branch','enrollment_number','phone_number', 'university')

        labels={
            'event_name' : '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'block': '',
            'branch': '',
            'enrollment_number': '',
            'phone_number': '',
            'university': '',

      
        }


        widgets= {
            'event_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Event Name / Company Name' }),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' First Name' }),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'} ),
            'block': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Block Name'}),
            'branch': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Branch\Course'}),
            'enrollment_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enrollment Number'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'university': forms.TextInput(attrs={'class':'form-control', 'placeholder':'University\College'}),

        }

from django.db import models
from django.db.models import manager
from django.db.models.fields import BLANK_CHOICE_DASH
from django.core.validators import RegexValidator

# Create your models here.
BLOCK_CHOICES = (
    ('A','A'),
   ('B','B'),('C','C'),  
)

class Event(models.Model):
    Image = models.ImageField(upload_to='pics')
    Date  =  models.DateTimeField('Date', blank=False)
    Name = models.TextField(max_length=30)
    Block = models.CharField(max_length=1,choices = BLOCK_CHOICES, default='A')
    cordinator = models.CharField(max_length=25)
    Discription = models.TextField(max_length=300)

    def __str__(self):
        return self.Name


class Placement(models.Model):
    Image = models.ImageField(upload_to='pics')
    Name = models.TextField(max_length=30)
    SOR =  models.DateTimeField('Start_of_Registration', blank=False)
    EOR =  models.DateTimeField('End_of_Registration', blank=False)
    Stream = models.TextField(max_length=100)
    CTC = models.CharField(max_length=20)
    Profile = models.CharField(max_length=20)
    Cordinator = models.CharField(max_length=25)
    Discription = models.TextField(max_length=500)

    def __str__(self):
        return self.Name

class user_registration(models.Model):
    alphanumeric = RegexValidator(r'^[a-z A-Z]*$', 'Only alphanumeric characters are allowed.')
    event_name = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    #event_name = models.CharField('event_name', max_length=122, blank=False)
    first_name =models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    last_name = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    email = models.EmailField('email', max_length=125)
    alpha = RegexValidator(r'^[A-C]*$', 'Only alphanumeric characters are allowed.')
    block = models.CharField(max_length=1, blank=True, null=True, validators=[alpha])
    branch = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    enrollment_number = models.CharField('enrollment_number', max_length=120)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{1,10}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 10, unique=False)
    university = models.CharField(max_length=100, blank=True, null=True, validators=[alphanumeric])
    
    def __str__(self):
        return self.first_name
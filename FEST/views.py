import calendar
from django.shortcuts import render
from datetime import datetime
from .models import Event, Placement,user_registration
from .forms import usersform
from django.http import HttpResponseRedirect

# Create your views here.
events = Event.objects.all()
placements = Placement.objects.all()
year = datetime.now().year
month = datetime.now().strftime('%B')
month_number = list(calendar.month_name).index(month)
month_number = int(month_number)


def nav(request):
    return render(request,'nav.html')

def home(request):
    #events = Event.objects.all()
    return render(request,'home.html',{'events': events})

def placement(request):
    return render(request,'placement.html', {'placements': placements})


def about(request):
    return render(request,'about.html')

def ablock(request):
    return render(request, 'ablock.html', {'events': events.filter(Block ='A')})

def bblock(request):
    return render(request, 'bblock.html', {'events': events.filter(Block ='B')})

def cblock(request):
    return render(request, 'cblock.html', {'events': events.filter(Block ='C')})

def register(request):
    submitted = False
    if request.method == "POST":
        form = usersform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = usersform
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'register.html', {'form':form, 'submitted':submitted})

    

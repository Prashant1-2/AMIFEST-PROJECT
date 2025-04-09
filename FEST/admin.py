from django.contrib import admin
from .models import Event,Placement,user_registration
# Register your models here.

admin.site.register(Event)
admin.site.register(Placement)
admin.site.register(user_registration)
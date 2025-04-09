from django.contrib import admin
from django.urls import path
from FEST import views

urlpatterns = [
    path('',views.home, name='home'),
    path('nav',views.nav, name='nav'),
    path('about',views.about, name='about'),
    path('placement',views.placement, name='placement'),
    path('ablock', views.ablock, name='ablock'),
    path('bblock', views.bblock, name='bblock'),
    path('cblock', views.cblock, name='cblock'),
    path('register', views.register, name='register'),
]

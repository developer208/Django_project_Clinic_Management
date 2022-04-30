
from os import name
from django.urls import path
from . import views



urlpatterns = [
   
    path('',views.homePage,name="home"),
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name="form"),
    path('book',views.book,name="book"),
    path('ad',views.admin,name="ad"),
    path('showtable',views.showtable,name="showtable"),
    path('patientlist',views.patient_list,name="patientlist"),
    path('contact',views.contact,name="contact"),

    path('del',views.delete,name="del"),
    
    
   
    
]
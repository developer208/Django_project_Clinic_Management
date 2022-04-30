from ast import Pass, Return
from email import message
from sqlite3 import Cursor
from turtle import clone

from urllib import request
from django.db import connection
import numpy as np
import email
from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from website.models import adminDetails,patientDetails,patientClone,truncate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail 


# Create your views here.

def homePage(request):  
    return render (request,'index.html')


def loginPage(request): 
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['passwd']
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("successfully logged in")
            return redirect('ad')

        else:
            return redirect('/')

    else:
        pass

    return render(request,'login.html')
    

def registerPage(request):
    pin1='2002'
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['emailid']
        pin = request.POST['pin']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username)
        print(email)
        print(pin)
        print(password1)
        if(pin ==pin1 ) and (password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('User Created')
        else:
            return redirect('/')
    

    return render(request, 'register.html')

        # if(password1 == password2) and (pin1==pin):
        #     user = adminDetails(username=username, password=password1, email=email)
        #     user.save()
        #     print('User Created')

        # else:
        #     return redirect('form')
            
                

    # if User.objects.filter(username=username).exists():
    #             messages.info(request, 'Username Taken')
    #             return redirect('homePage')
    # else:
    #             user = User.objects.create_user(username=username, password=password1, email=email)
    #             user.save()
    #             print('User Created')

    return render(request,'registerform.html')

def book(request):
    if request.method =='POST':
        v1=request.POST['your_name']
        v2=request.POST['phone']
        v3=request.POST['mail']
        v4=request.POST['rb']
        print(v1)
        print(v2)
        print(v3)
        print(v4)
        if v1!=''and v2!=''and v3!=''and v4!='':
            send_mail(
            'django mail service',
            'appointment booked ',
            'it.developer2002@gmail.com',
            [v3],
            fail_silently=False
            ) 
        patient=patientDetails(name=v1,phone_number=v2,email=v3,gender=v4)
        clone=patientClone(name=v1,phone_number=v2,email=v3,gender=v4)
        clone.save()
        patient.save()
        return redirect('/')

        

    else:
        pass  
    return render(request,'book.html')

def admin(request): 
    temp=0
    temp1=0
    
    current=0
    current1=0
    status="-"
    patient1=patientDetails.objects.all()
    if request.method == 'POST':
        e = request.POST['email']
        print(e)
       

        
        # current1=int(current)-1
        # previous=current-1
        message='doctor is checking '+'patient :'+str(e)
        if e=='':
            print(type(current))
            print(type(e))
            print(type(current1))
            print(type(temp1))
            print('null')
            status="Enter patient no :"
            
            
        else:
            print(message)
            current=e
            temp1=int(e)
            current1=temp1-1
            delete_record=patientClone.objects.get(id=e)
            delete_record.delete()
            patient2=patientClone.objects.values_list('email')
            for v in patient2:
                send_mail(
                'django mail service',
                message,
                'it.developer2002@gmail.com',
                [v[temp]],
                fail_silently=False
                ) 
                print("mail send")
                print(current)
                print(current1)
            e=''
                
                
            status="Sucessfullly sent"
            
            
    else:
        print("fail")
        status="failed"

    print(status)
    

    
    return render(request,'admin.html',{'dbvalue':patient1,'status':status,'previous':current1,'current':current})

# def fetchdata(request):
#     patient=patientDetails.objects.all()
#     if request.method=='post':
#         temp=request.post('feild1')
#         print(temp)
#     else:
#         pass
   
#     return render (request,'datafetch.html',{'dbvalue':patient})

def showtable(request):
    return render(request,'t.html')

def patient_list(request):
    temp=0
    patient1=patientDetails.objects.all()
    patient2=patientDetails.objects.values_list('email')
    # print(type(patient2))
    # print(type(patient1))
    
    

        # for v in patient2:
        # arr=np.asarray(v)
        # print(temp)
        # print(v[temp])
        # temp=temp+1
        # print(temp)

        
        

        
        # send_mail(
        #     'django mail service',
        #     'doctor is checking {{}}patient',
        #     'it.developer2002@gmail.com',
        #     [v[temp]],
        #     fail_silently=False
        #     ) 
        # print("send")
    return render (request,'patient_list.html',{'dbvalue':patient1})
    

    
   
def delete(request):
    # patientClone.objects.raw('truncate website_patientclone ;')
    # patientDetails.objects.raw('truncate website_patientdetails ;')
    # patientClone.objects.all().delete()
    # patientDetails.objects.all().delete()
    

    return HttpResponse('table truncated')

def contact(request):
    return render(request,'contact.html')

def delete(request):
     patientClone.objects.all().delete()
     patientDetails.objects.all().delete()
     return redirect('ad')

            
    
    










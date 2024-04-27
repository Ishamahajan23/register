from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from app1.models import Join_users
from app1.models import contact
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import mysql.connector as sql
from channels.layers import get_channel_layer
import json
from time import gmtime, strftime
from django.template import RequestContext
from plyer import notification
import time
from asgiref.sync import async_to_sync
# Create your views here.

@login_required(login_url='login')


def HomePage(request):
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     "notification_broadcast",
    #     {
    #         'type': 'send_notification',
    #         'message': json.dumps("Notification")
    #     }
    # )
    return render(request,'index2.html',{
         'room_name':"broadcast"

     }) 

def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")

def SignupPage(request):
 
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:

            return render(request,'registration.html',{'form':request.POST,'error_massage':'invalid email or password. Please re-enter'})
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

        
        

    return render(request,'registration.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'form':request.POST,'error_massage':'invalid email or password. Please re-enter'})


    return render(request,'login.html')

def LogoutPage(request):
     logout(request)
     return redirect('login')

def AboutPage(request):
    return render(request,'about.html')

def NotificationPage(request):
    
   
    return render(request,'notification.html')

def ContactPage(request):
    n=''
    if request.method=='POST':
        email=request.POST.get('email')
        mobilenumber=request.POST.get('mobilenumber')
        message=request.POST.get('message')
        user=contact(email=email,mobilenumber=mobilenumber,message=message)
        user.save()
        n='Thanks For sharing your Feedback'
    return render(request,'contact.html',{'n':n})

def JoinPage(request):
    n=''
    if request.method=='POST':
        username=request.POST.get('name')
        useremail=request.POST.get('email')
        userage=request.POST.get('age')
        userlocation=request.POST.get('location')
        userinterests=','.join(request.POST.getlist('interests[]'))
        userschedule=request.POST.get('schedule')
        userfrequency=request.POST.get('frequency')
        usertypes=','.join(request.POST.getlist('types[]'))
    
        user=Join_users(username=username,email=useremail,age=userage,location=userlocation,interests=userinterests,schedule=userschedule,frequency=userfrequency,types=usertypes)
        user.save()
        n='Data inserted sucessfully Now your notifications are started'
        # return redirect('notification')
   

    return render(request,'joinform.html',{'n':n})


def FrontPage(request):
    return render(request,'index.html',{
         'room_name':"broadcast"

     })

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def index(request):
     return render(request,"userside/index.html")

def user_register(request):
     if request.method == "POST":
          uname=request.POST.get('username')
          email=request.POST.get('email')
          pass1=request.POST.get('password1')
          pass2=request.POST.get('password2')
              
          if pass1!=pass2:
               return HttpResponse("your passwords are not same")
          else:
               
               my_user=User.objects.create_user(username=uname,email=email,password=pass1)
               my_user.save()
               return redirect('/user-login')

     return render (request,'userside/user_register.html')


def user_login(request):
     if request.method == "POST":
          username=request.POST.get('username')
          pass1=request.POST.get('pass')
          user=authenticate(request,username=username,password=pass1)
          if user is not None: 
               login(request,user)
               return redirect('/index')
          else:
                return HttpResponse("Username or Password is incorrect")

     return render (request,'userside/user_login.html')


def user_logout(request):
     logout(request)
     return redirect('/index')

def banner_image(request):
     return render(request, 'layout.html')


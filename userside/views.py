from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.


def index(request):
     return render(request,'userside/index.html')

def user_register(request):
     if request.method == "POST":
          U = User.objects.create_user(
               username=request.POST[''],
               email=request.POST['email'],
               password=request.POST['password']
          )
          messages.success(request, "Account Created Successfull")
          return render(request, 'userside/user_register.html')
     else:
          messages.warning(request, "Something Went Wrong, Please Try Again")
          return render(request, 'userside/user_register.html')

def user_login(request):
     if request.session.has_key('is_logged'):
          return redirect('user-register')
     
     if request.method == "POST":
          result = authenticate(username=request.POST['email'], password=request.POST['password'])
          print(result)
          if result is not None:
               if not result.is_superuser:
                    request.session['is_logged'] = True
                    login(request, result)
                    messages.success(request, "Login Succesfull")
                    return redirect(user_register)
               else:
                    messages.error(request, "Wromg Username And Password")
                    return render(request, 'userside/user_login.html')
          else:
               messages.error(request, "Wrong Username And Password")
               return render(request, 'userside/user_login.html')
     else:
          return render(request, 'userside/user_login.html')  
     
def banner_image(request):
     return render(request, 'layout.html')

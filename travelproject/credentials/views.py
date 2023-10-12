from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .models import Team

# # Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        Email = request.POST['email']
        Password = request.POST['password']
        Cpassword = request.POST['password2']
        if Password == Cpassword:
               if User.objects.filter(username=username).exists():
                   messages.info(request,'user already exist')
                   return redirect('register')
               elif User.objects.filter(email=Email).exists():
                   messages.info(request,"email already exist")
                   return redirect('register')
               else:
                   user = User.objects.create_user(username=username,first_name=firstName,last_name=lastName,email=Email,password=Password)
                   user.save();
                   # return redirect('login')


        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('login')

    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

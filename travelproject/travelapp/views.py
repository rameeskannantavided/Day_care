from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Team




def demo(request):
    name = 'ramees'
    team_members = Team.objects.all()  # Fetch all Team objects from the database
    return render(request, 'index.html', {'result': team_members})






def about(request):
    return render(request,'about.html')
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
                   return redirect('regsier/')
               elif User.objects.filter(email=Email).exists():
                   messages.info(request,"email already exist")
                   return redirect('regsier/')
               else:
                   user = User.objects.create_user(username=username,first_name=firstName,last_name=lastName,email=Email,password=Password)
                   user.save()


        else:
            messages.info(request,"password not matching")
            return redirect('/')

    return render(request,'register.html')

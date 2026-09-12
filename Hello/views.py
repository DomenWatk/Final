from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from Hello.models import Stockheld
from django.contrib.auth import logout,login,aauthenticate
import yfinance as yf
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from Hello.Forms.Form import ExtendedSignupForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



def home(request):
    current_year=timezone.now().year
    return render(request, 'Template.html', {'current_year': current_year })

def Stockinput(request):
    if request.method == 'POST':
        Stockheldform = Stockheld(request.POST)
        if Stockheldform.is_valid():
            Stockheldform.save()
            return HttpResponse('Stock held data saved successfully.')
    else:
        form = Stockheld()

    return render(request, 'Template.html', {'form': form})

def Signup_view(request):
    if request.method == 'POST':
        form=ExtendedSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExtendedSignupForm()

        
    
    return render(request, "Signup.html", {'form':form})



def Signin_view(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,'Signin successful')
            return redirect('home')
    else:
        form=AuthenticationForm()

    return render(request,'Signin.html',{'form':form})

def logout(request):
    if request.method =="POST":
        logout(request)
        return redirect('home')
    
    

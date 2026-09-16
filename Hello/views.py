from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib.auth import logout,login,aauthenticate
import yfinance as yf
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from Hello.Forms.Form import ExtendedSignupForm, BankStatementForm,Stocksheldinput
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import datetime
import tabula
from django.contrib.auth.decorators import login_required
@login_required

def current_year(request):
    return{'current_year':datetime.now().year}

def home(request):
    current_year=timezone.now().year
    return render(request, 'Template.html', {'current_year': current_year })



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

def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect('home')

def Assets_view(request):
    if request.method=="POST":
        form=Stocksheldinput(request.POST)
        if form.is_valid():
            Stocks=form.save(commit=False)
            Stocks.user=request.user
            form.save()
            return redirect('Assets')
    else:
        form=Stocksheldinput()
    
    
    return render(request,'Assets.html',{'form': form})
def Finance_view(request):
    form=BankStatementForm(request.POST,request.FILES)
    if form.is_valid():
                statement=form.save(commit=False)
                statement.user=request.user
                statement.save()
                return redirect('Assets')
    else:
            form=BankStatementForm()
    return render(request,'Finance.html',{'form':form})


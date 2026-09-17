from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib.auth import logout,login,aauthenticate
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from Hello.Forms.Form import ExtendedSignupForm, BankStatementForm,Stocksheldinput
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
from .models import Stocksheld
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



def Assets_view(request):
    if request.method == "POST":
        form = Stocksheldinput(request.POST)

        if form.is_valid():
            stock_name = form.cleaned_data['Stockname']
            amount = form.cleaned_data['Amountheld']
            average_cost = form.cleaned_data['Averagecost']

            stock = Stocksheld.objects.filter(
                user=request.user,
                Stockname=stock_name
            ).first()

            if stock:
                # Stock already exists
                old_amount=stock.Amountheld 
                old_average=stock.Averagecost
                new_amount=old_amount+amount
                new_average=(
                     (old_amount*old_average)+
                     (amount*average_cost)
                )/new_amount
                stock.Amountheld=new_amount
                stock.Averagecost=new_average
                stock.save()

            else:
                # Stock doesn't exist, create it
                stock = form.save(commit=False)
                stock.user = request.user
                stock.save()

            return redirect('Assets')

    else:
        form = Stocksheldinput()

    Assets = Stocksheld.objects.filter(user=request.user)

    return render(request, 'Assets.html', {
        'form': form,
        'Assets': Assets
    })

    
    return render(request,'Assets.html',{'form': form,'Assets':Assets})
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


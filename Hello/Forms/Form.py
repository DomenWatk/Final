from django import forms
from Hello.models import Stocksheld,Bankstatement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ExtendedSignupForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={"class": "form-control"})
)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class BankStatementForm(forms.ModelForm):
    description = forms.CharField(required=True)
    amount = forms.FloatField(required=True)
    class Meta:
        model= Bankstatement
        fields=['description','amount']
class Stocksheldinput(forms.ModelForm):
    Stockname =forms.CharField(required=True)
    Amountheld =forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'step':'any'}))
    Averagecost=forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'step':'any'}))
    class Meta:
        model=Stocksheld
        fields=['Stockname','Amountheld','Averagecost']
     
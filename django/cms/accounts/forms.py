from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from accounts.models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['email','username','password1','password2']
    
class OrderForm(forms.ModelForm):
    
    class Meta:
        model=Order
        fields='__all__'
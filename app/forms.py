from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
       model=User
       fields={'username','email'}
       widgets={'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={ 'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label="Password",strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


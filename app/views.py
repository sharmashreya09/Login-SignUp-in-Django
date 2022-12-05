from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def Home(request):
    return render(request,'home.html')

class SignUp(View):
    def get(self,request):
        fm=SignUpForm()
        return render(request, 'signup.html',{'form':fm})

    def post(self,request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"SignUp Success")
            return redirect("/signup")
        else:
            return render(request, 'signup.html', {'form': fm})


class Login(View):
    def get(self,request):
        fm=LoginForm()
        return render(request,'login.html',{'form':fm})

    def post(self,request):
        fm=LoginForm(request,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                 login(request, user)
                 return redirect('/')

            else:
                return render(request, 'login.html', {'form': fm})


        else:
            return render(request, 'login.html', {'form': fm})








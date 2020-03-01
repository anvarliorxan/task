from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import logging



def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        newUser = User(username= username,email= email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect('index')
    return render(request,'register.html',{'form':form})


def loginUser(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username =username ,password = password)

        if user is None:
            messages.success(request,'istifadəçi adınız və ya şifrəniz yalnışdır')
            return render(request,'login.html',{'form':form})
        messages.success(request,'Daxil oldunuz')
        login(request,user)
        return redirect('index')

    return render(request,'login.html',{'form':form})


def logoutUser(request):
    logout(request)
    messages.success(request,'Sistemden Cixdiniz')
    return redirect('index')

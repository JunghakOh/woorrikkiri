from django.shortcuts import render, redirect
from django.utils import timezone
from django import forms
from .forms import UserRegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = UserRegisterForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            return redirect('home')
    else:
        signup_form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

def signout(request):
    auth.logout(request)
    return render(request, 'main/home.html')
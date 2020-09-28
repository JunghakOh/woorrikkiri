from django.shortcuts import render, redirect
from django.utils import timezone
from django import forms
from .forms import UserRegisterForm, LoginForm, ProfileForm
from main.forms import ContentForm, CommentForm, AnswerForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from main.models import Content, Comment, Answer, FAQ


# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = UserRegisterForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user) #프로필 생성
            return redirect('home')
        else:
            # 메시지 띄우기
            messages.error(request, "이미있는 아이디거나 입력한 정보가 정확하지 않습니다.")
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
            messages.error(request, "아이디가없거나비밀번호가일치하지않습니다.")
            form = LoginForm()
            return render(request, 'accounts/signin.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    auth.logout(request)
    return render(request, 'main/home.html')

@login_required
def mypage(request):
    posts = Content.objects.all().order_by('-pub_date')
        #post_list = post.filter(name=request.user.name)            
    return render(request, 'accounts/mypage.html', {'posts_list':posts})

def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('mypage')
    else:
        profile_form = ProfileForm()
    return render(request, 'accounts/profile_update.html', {'profile_form':profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('mypage')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required
def user_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'accounts/user_delete.html')

from django import forms
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from main.models import Content, Comment, Answer, FAQ

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=10)
    #student_num = forms.CharField(max_length=30)
    school = forms.CharField(max_length=15)
    phone_num = forms.CharField(max_length=20)
    #account_num = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        models = get_user_model()
        fields = ['username', 'name', 'email', 'school', 'phone_num', 'gender', 'is_mento',]
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password',]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['introduction', 'profile_photo',]
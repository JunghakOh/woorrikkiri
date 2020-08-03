from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content


# Create your views here.
def home(request):
    posts = Content.objects.all
    return render(request, 'main/home.html', {'posts_list':posts})
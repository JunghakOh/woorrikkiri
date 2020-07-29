from django import forms
from .models import Content, Comment

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'body', ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text',]
from django import forms
from .models import Content, Comment, Answer

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'body', 'file' ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('author', 'text',)
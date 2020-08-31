from django import forms
from .models import Content, Comment, FAQ, Answer

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'subjects', 'body', 'file',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['title', 'body',]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body', 'file', ]

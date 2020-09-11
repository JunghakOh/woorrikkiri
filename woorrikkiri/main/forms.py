from django import forms
from .models import Content, Comment, FAQ, Answer, Subject

class ContentForm(forms.Form):
    class Meta:
        model = Content
        model = Subject
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

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subjects', ]
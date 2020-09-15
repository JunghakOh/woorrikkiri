from django import forms
from .models import Content, Comment, FAQ, Answer, Subject, Point

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'subjects', 'coffee', 'body', 'file',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text",]

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

class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['points', ]

class ApproveForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['approve', ]
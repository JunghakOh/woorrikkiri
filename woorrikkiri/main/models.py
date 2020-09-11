from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.
class Content(models.Model):
    SUBJECTS_COMPUTING = 'c'
    SUBJECTS_BASICC = 'b'
    SUBJECTS_GC = 'g'
    CHOICES_SUBJECTS = (
        (SUBJECTS_COMPUTING, '컴퓨팅 사고력'),
        (SUBJECTS_BASICC, '기초 C언어'),
        (SUBJECTS_GC, '고급응용 C프로그래밍'),
    )

    objects = models.Manager()
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = "작성자", on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    subjects = models.CharField("과목", max_length=1, choices=CHOICES_SUBJECTS)
    body = models.TextField(default='')
    file = models.FileField(upload_to='documents/%Y, %m/', blank=True)
    
class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)

class FAQ(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')

class Answer(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    body = models.TextField(default='')
    pub_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='documents/%Y, %m/', blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = "작성자", on_delete = models.CASCADE)


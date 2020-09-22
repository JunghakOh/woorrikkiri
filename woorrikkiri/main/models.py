from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.
class Content(models.Model):
    SUBJECTS_COMPUTING = 'computing'
    SUBJECTS_BASICC = 'basicC'
    SUBJECTS_GC = 'GC'
    SUBJECTS_BASICENGINEERING = 'basicEngineering'
    SUBJECTS_UNIVMATH = 'univMath'
    SUBJECTS_PRINCIPLESOFECONOMICS1 = 'principlesodEconomics1'
    SUBJECTS_PRINCIPLESOFECONOMICS2 = 'principlesodEconomics2'
    CHOICES_SUBJECTS = (
        (SUBJECTS_COMPUTING, '컴퓨팅 사고력'),
        (SUBJECTS_BASICC, 'C언어 기초'),
        (SUBJECTS_GC, '고급응용 C프로그래밍'),
        (SUBJECTS_BASICENGINEERING, '기초공학설계'),
        (SUBJECTS_UNIVMATH, '대학수학'),
        (SUBJECTS_PRINCIPLESOFECONOMICS1, '경제학원론1'),
        (SUBJECTS_PRINCIPLESOFECONOMICS2, '경제학원론2'),

    )

    subjects = models.CharField("과목", max_length=30, choices=CHOICES_SUBJECTS)
    objects = models.Manager()
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name ='writer', verbose_name = "작성자", on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    coffee = models.IntegerField("커피", default = 0)
    file = models.FileField(upload_to='documents/%Y, %m/', blank=True)
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, related_name ='respondent', verbose_name = "답변자", on_delete = models.CASCADE, null=True)
    
class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = "작성자", on_delete = models.CASCADE)

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
    #respondent = models.

class Subject(models.Model):
    SUBJECTS_COMPUTING = 'computing'
    SUBJECTS_BASICC = 'basicC'
    SUBJECTS_GC = 'GC'
    SUBJECTS_BASICENGINEERING = 'basicEngineering'
    SUBJECTS_UNIVMATH = 'univMath'
    SUBJECTS_PRINCIPLESOFECONOMICS1 = 'principlesodEconomics1'
    SUBJECTS_PRINCIPLESOFECONOMICS2 = 'principlesodEconomics2'
    CHOICES_SUBJECTS = (
        (SUBJECTS_COMPUTING, '컴퓨팅 사고력'),
        (SUBJECTS_BASICC, 'C언어 기초'),
        (SUBJECTS_GC, '고급응용 C프로그래밍'),
        (SUBJECTS_BASICENGINEERING, '기초공학설계'),
        (SUBJECTS_UNIVMATH, '대학수학'),
        (SUBJECTS_PRINCIPLESOFECONOMICS1, '경제학원론1'),
        (SUBJECTS_PRINCIPLESOFECONOMICS2, '경제학원론2'),

    )

    objects = models.Manager()
    subjects = models.CharField("과목", max_length=30, choices=CHOICES_SUBJECTS)

class Point(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Content', on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField("포인트", default = 0)
    account_num = models.CharField("계좌번호", max_length=30, null=True, blank=True)
    point_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "포인트사용자", on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    approve = models.BooleanField("결제승인", default=False)
    coupon= models.IntegerField("커피", default = 0)
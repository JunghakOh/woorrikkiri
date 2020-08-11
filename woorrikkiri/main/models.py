from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.conf import settings

# Create your models here.
class Content(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
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
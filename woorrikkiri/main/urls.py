from django.conf.urls import urls
from . import views

url(r'^getJobState$', views.getJobState, name='GetJobState')
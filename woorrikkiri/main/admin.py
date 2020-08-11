from django.contrib import admin
from .models import Content, Comment, FAQ
# Register your models here.

admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(FAQ)
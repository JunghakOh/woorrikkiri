from django.contrib import admin
from .models import Content, Comment, FAQ, Answer, Point
# Register your models here.

admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(FAQ)
admin.site.register(Answer)
admin.site.register(Point)
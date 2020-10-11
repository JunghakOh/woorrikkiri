from django.contrib import admin
from . import models

@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'subjects',
        'writer',
        'body',
        'coffee',
        'respondent',
        'pub_date'
    )
    list_display_links = (
        'title',
        'writer',
        'respondent'
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'text',
        'writer',
        'created_date'
    )
    list_display_links = (
        'post',
        'text',
        'writer'
    )

@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
    )
    list_display_links = (
        'title',
    )

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'post',
        'writer',
        'pub_date'
    )
    list_display_links = (
        'body',
        'post',
        'writer'
    )

@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'points',
        'point_user',
        'pub_date',
        'account_num',
        'approve',
    )
    list_display_links = (
        'post',
        'points',
        'point_user'
    )
# admin.site.register(Content)
# admin.site.register(Comment)
# admin.site.register(FAQ)
# admin.site.register(Answer)
# admin.site.register(Point)
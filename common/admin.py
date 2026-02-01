from django.contrib import admin

from common.models import Comment, Like


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ...
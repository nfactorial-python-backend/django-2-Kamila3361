from django.contrib import admin

from .models import News, Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 5

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at', 'has_comments']
    inlines = [CommentInLine]

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
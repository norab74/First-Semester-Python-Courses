from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'pub_date', 'post_likes')
    search_fields = ('post_title', 'post_contents')
    ordering = ('-pub_date',)
    
@admin.register(CommentOnPost)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'pub_date', 'approved')
    list_filter = ('approved', 'pub_date', 'post')
    search_fields = ('name', 'comment_contents')
    
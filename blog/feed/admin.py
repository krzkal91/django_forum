from django.contrib import admin

# Register your models here.

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'publishing_time', 'last_update_time', 'is_published', 'content')
    list_editable = ('is_published', 'content')

admin.site.register(Comment)
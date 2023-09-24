# In your app's admin.py

from django.contrib import admin
from .models import Post, Comment, UserProfile, Tag
class CommentInline(admin.TabularInline):  # Create an inline for comments
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on')
    list_filter = ('post', 'author')
    search_fields = ('content', 'author__username', 'post__title')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Tag, TagAdmin)

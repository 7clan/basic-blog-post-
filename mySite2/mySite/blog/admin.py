from django.contrib import admin
from .models import BlogPost, Author,tag, Comment
# Register your models here.



admin.site.register(BlogPost, list_display=('title', 'created_at'))
admin.site.register(Author, list_display=('name', 'email'))
admin.site.register(tag, list_display=('name', 'slug'))
admin.site.register(Comment, list_display=('post', 'author', 'created_at'))
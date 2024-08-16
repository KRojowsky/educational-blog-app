from django.contrib import admin
from .models import BlogPost, BlogCategory

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category')
    list_filter = ('created_at', 'category')
    search_fields = ('title', 'content')
    fields = ('title', 'slug', 'author', 'content', 'category', 'image')
    exclude = ('created_at',)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)

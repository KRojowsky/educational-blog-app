from django.contrib import admin
from .models import BlogPost, BlogCategory, ContentBlock

class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 1

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category', 'is_new', 'is_trending', 'slug')
    list_filter = ('created_at', 'category', 'is_new', 'is_trending')
    search_fields = ('title', )
    fields = ('title', 'author', 'category', 'image', 'slug', 'is_new', 'is_trending')
    inlines = [ContentBlockInline]
    prepopulated_fields = {"slug": ("title",)}

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)

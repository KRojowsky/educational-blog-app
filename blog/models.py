from django.db import models
from django.contrib.auth.models import User

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_posts')
    is_new = models.BooleanField(default=False, verbose_name='Nowość')
    is_trending = models.BooleanField(default=False, verbose_name='Na czasie')
    content = models.TextField()

    def __str__(self):
        return self.title


class ContentBlock(models.Model):
    TEXT = 'text'
    IMAGE = 'image'
    
    BLOCK_TYPE_CHOICES = [
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
    ]
    
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='content_blocks')
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPE_CHOICES)
    order = models.PositiveIntegerField()
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_content_images/', blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Block {self.id} ({self.get_block_type_display()}) for {self.blog_post.title}"
    
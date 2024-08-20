from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import BlogPost, BlogCategory


def get_blog_context():
    categories = BlogCategory.objects.all()
    years = BlogPost.objects.dates('created_at', 'year').distinct()
    months = BlogPost.objects.dates('created_at', 'month').distinct()
    days = BlogPost.objects.dates('created_at', 'day').distinct()
    
    return {
        'categories': categories,
        'years': years,
        'months': months,
        'days': days,
    }


def blog_post_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    new = request.GET.get('new')
    trending = request.GET.get('trending')

    blog_posts = BlogPost.objects.all()

    if category_id:
        category = get_object_or_404(BlogCategory, id=category_id)
        blog_posts = blog_posts.filter(category=category)
    
    if query:
        blog_posts = blog_posts.filter(Q(title__icontains=query))
    
    if start_date and end_date:
        blog_posts = blog_posts.filter(created_at__range=[start_date, end_date])
    
    if year:
        blog_posts = blog_posts.filter(created_at__year=year)
    
    if month:
        blog_posts = blog_posts.filter(created_at__month=month)
    
    if day:
        blog_posts = blog_posts.filter(created_at__day=day)
    
    if new:
        blog_posts = blog_posts.filter(is_new=True)
    
    if trending:
        blog_posts = blog_posts.filter(is_trending=True)

    blog_posts = blog_posts.order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(blog_posts, 12)
    blog_posts = paginator.get_page(page)

    context = get_blog_context()
    context.update({
        'blog_posts': blog_posts,
    })

    return render(request, 'blog/blog_post_list.html', context)



def blog_post_detail(request, slug, id):
    post = get_object_or_404(BlogPost, slug=slug, id=id)
    post.increment_views()
    content_blocks = post.content_blocks.all()
    similar_posts = post.get_similar_posts().order_by('-created_at')[:4]

    context = get_blog_context()
    context.update({
        'post': post,
        'content_blocks': content_blocks,
        'similar_posts': similar_posts,
    })

    return render(request, 'blog/blog_post_detail.html', context)

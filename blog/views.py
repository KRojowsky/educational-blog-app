from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import BlogPost, BlogCategory
from django.utils.dateparse import parse_date


def blog(request):
    return render(request, 'base-blog.html')


def blog_post_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')

    blog_posts = BlogPost.objects.all()
    categories = BlogCategory.objects.all()

    if category_id:
        category = get_object_or_404(BlogCategory, id=category_id)
        blog_posts = blog_posts.filter(category=category)
    
    if query:
        blog_posts = blog_posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    if start_date and end_date:
        blog_posts = blog_posts.filter(created_at__range=[start_date, end_date])
    
    if year:
        blog_posts = blog_posts.filter(created_at__year=year)
    
    if month:
        blog_posts = blog_posts.filter(created_at__month=month)
    
    if day:
        blog_posts = blog_posts.filter(created_at__day=day)

    blog_posts = blog_posts.order_by('-created_at')

    years = BlogPost.objects.dates('created_at', 'year').distinct()
    months = BlogPost.objects.dates('created_at', 'month').distinct()
    days = BlogPost.objects.dates('created_at', 'day').distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(blog_posts, 6)
    blog_posts = paginator.get_page(page)

    context = {
        'blog_posts': blog_posts,
        'categories': categories,
        'years': years,
        'months': months,
        'days': days,
    }
    return render(request, 'blog/blog_post_list.html', context)

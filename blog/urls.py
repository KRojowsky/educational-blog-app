from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_post_list, name='blog_post_list'),
]
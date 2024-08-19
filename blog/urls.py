from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_post_list, name='blog_post_list'),
    path('<slug:slug>/<int:id>/', views.blog_post_detail, name='blog_post_detail'),
]

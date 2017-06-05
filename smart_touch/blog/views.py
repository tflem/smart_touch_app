from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """Retrieves all posts witin published status using manager"""
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    """Retrieves post data with given parameters."""
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

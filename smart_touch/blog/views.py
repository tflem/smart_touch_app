from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    """Retrieves all posts witin published status using manager"""
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page not integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                  'posts': posts})

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

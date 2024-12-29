from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost, Comment # Import your BlogPost model
from .forms import CommentForm
from django.utils import timezone

# Create your views here.
def index(request):
    # Fetch the welcoming page of the site
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/index.html', {'blog_posts': blog_posts})


def blogpost(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/blogpost.html', {'blog_posts': blog_posts})


def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    comments = blog_post.comments.all()  # Related comments
    images = blog_post.images.all()      # Related images

    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:
            Comment.objects.create(
                blog_post=blog_post,
                author=request.user,
                content=content,
                created_at=timezone.now()
            )
            return redirect('blog_detail', pk=pk)  # Redirect to the same blog post page

    return render(request, 'IDGenie/blog_detail.html', {
        'blog_post': blog_post,
        'comments': comments,
        'images': images,
    })
    
    
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def get_user_avatar(request):
    avatar_url = request.user.profile.avatar.url if request.user.profile.avatar else "/path/to/default-avatar.png"
    return JsonResponse({"avatar_url": avatar_url})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost, Comment # Import your BlogPost model
from .forms import CommentForm
from django.utils import timezone
from django.utils import timezone

# Create your views here.
def index(request):
    # Fetch the welcoming page of the site
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/index.html', {'blog_posts': blog_posts})


def blogpost(request):
    blog_posts = BlogPost.objects.prefetch_related('comments').all()
    return render(request, 'IDGenie/blogpost.html', {'blog_posts': blog_posts})

def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    comments = blog_post.comments.all()
    paragraphs = blog_post.paragraphs.all()  # Related paragraphs
    images = blog_post.images.all()          # Related images
    quotes = blog_post.quotes.all()          # Related quotes

    # Check if the video_url is available and transform it
    if blog_post.video_url:
        # Replace 'watch?v=' with 'embed/' for the YouTube embed URL
        blog_post.video_embed_url = blog_post.video_url.replace('watch?v=', 'embed/')
    else:
        blog_post.video_embed_url = None  # If no video URL, set it to None

    # Handle comment submission
    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:
            Comment.objects.create(
                blog_post=blog_post,
                author=request.user,
                content=content,
                created_at=timezone.now()
            )
            return redirect('blog_detail', pk=pk)

    # Pass all data to the template
    return render(request, 'IDGenie/blog_detail.html', {
        'blog_post': blog_post,
        'comments': comments,
        'paragraphs': paragraphs,
        'images': images,
        'quotes': quotes,
    })
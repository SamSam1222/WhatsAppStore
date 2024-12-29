from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost, Comment # Import your BlogPost model
from .forms import CommentForm

# Create your views here.
def index(request):
    # Fetch the welcoming page of the site
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/index.html', {'blog_posts': blog_posts})


def blogpost(request):
    blog_posts = BlogPost.objects.prefetch_related('comments').all()
    return render(request, 'IDGenie/blogpost.html', {'blog_posts': blog_posts})


def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    comments = blog_post.comments.all()  # Fetch comments related to the post
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:  # Ensure content is not empty
            Comment.objects.create(
                blog_post=blog_post,
                author=request.user,
                content=content,
                created_at=timezone.now()
            )
            return redirect('blog_post_detail', pk=pk)

    return render(request, 'blog/post_detail.html', {
        'blog_post': blog_post,
        'comments': comments
    })

# def blogpost(request):
#     # Fetch all blog posts
#     posts = BlogPost.objects.all()
#     return render(request, 'IDGenie/blogpost.html', {'posts': posts})

# def blog_detail(request, post_id):
#     blog_post = get_object_or_404(BlogPost, id=post_id)
#     comments = blog_post.comments.all() # Get all comments for this blog post
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog_post = blog_post
#             comment.author = request.user   # Assuming the user is logged in
#             comment.save()
#             return redirect('IDGenie:blog_detail', post_id=post_id)
#         else:
#             form = CommentForm()
#         return render(request, 'IDGenie/blog_detail.html', {'blog_post': blog_post, 'comments': comments, 'form': form})
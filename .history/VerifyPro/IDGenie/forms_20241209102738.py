from django.shortcuts import render, redirect
from .models import BlogPost, Comment
from django.contrib.auth.models import User # for the author field
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm # If you are using forms.py
from django.http import HttpResponse


# Blog post detail view
def blog_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    recent_posts = post.get_recent_posts() # Get recent posts
    comments = post.comments.all() # Get comments for this post
    
    if request.method == "POST":
        comment = Comment()
        comment.blog_post = post
        comment.name = request.POST['name']
        comment.email = request.POST['email']
        comment.content = request.POST['content']
        comment.save()
        return redirect('IDGenie:blog_detail', post_id=post.id)
    
    return render(request, 'IDGenie/blog_detail.html', {
        'post': post,
        'recent_posts': recent_posts,
        'comments': comments
    })
    
# Blog post list view
def blogpost(request):
    posts = BlogPost.objects.all()
    return render(request, 'IDGenie/blog.html', {'posts': posts})


# Blog post create view (for users to submit posts)
@login_required
def create_blog_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        quote_or_video = request.POST('quote_or_video')
        
        # Create the blog post
        blog_post = BlogPost.objects.create(
            title=title,
            content=content,
            image=image, 
            quote_or_video=quote_or_video,
            author=request.user,
        )
        return redirect('IDGenie:blog')
    
    return render(request, 'IDGenie/create_blog_post.html')

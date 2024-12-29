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
    return render(request, 'IDGenie/index.html')


def blogpost(request):
    # Fetch all blog posts
    posts = BlogPost.objects.all()
    return render(request, 'IDGenie/blogpost.html', {'posts': posts})

def blog_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    comments = blog_post.comments.all() # Fetch all comments related to the blog post
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = blog_post
            comment.user = request.user
            comment.save()
            return redirect('IDGenie:blog_detail', post_id=blog_post.id)
        
        
        context = {
            'blog_post': blog_post,
            'comments': comments,
            'form': form,
        }
        return render(request, 'IDGenie/blog_detail.html', context)
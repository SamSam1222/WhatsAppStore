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
    comment = blog_post.comments.all() # Get all comments for this blog post
    if request.(self, *args, **kwargs):
        return super().(*args, **kwargs)
    
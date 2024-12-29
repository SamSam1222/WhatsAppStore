from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost


# Create your views here.
def index(request):
    # Fetch the welcoming page of the site
    return render(request, 'IDGenie/index.html')


def blogpost(request):
    # Fetch all blog posts
    posts = BlogPost.objects.all()
    return render(request, 'IDGenie/blogpost.html', {'posts': posts})

def blog_detail(request, post_id):
    # Fetch a single blog post by its id or return 404 if not found
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'IDGenie/blog_detail.html', {'post': post})
    
    
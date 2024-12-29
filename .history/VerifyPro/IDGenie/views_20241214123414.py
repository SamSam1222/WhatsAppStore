from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost # Import your BlogPost model
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # Example of using reverse to redirect to the same index page
    url = reverse('IDGenie:index')  # Reverse the URL for the index view
    print("Resolved URL:", url)  # Debugging: print resolved URL to console

    # Render the index page
    return render(request, 'IDGenie/index.html')

def blogpost(request):
    # Fetch all blog posts
    posts = BlogPost.objects.all()
    return render(request, 'IDGenie/blogpost.html', {'posts': posts})

def blog_detail(request, post_id):
    # Fetch a single blog post by its id or return 404 if not found
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'IDGenie/blog_detail.html', {'post': post})
    
    
# Blog Post Create View
@login_required
def create_blog_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content =request.POST.get('content')
        image = request.FILES.get('image') # File input for the image
        quote_or_video = request.POST.get('quote_or_video', '') # Optional quote or video embed
        
        # Create the blog post
        blog_post = BlogPost.objects.create(
            title=title,
            content=content,
            image=image,
            quote_or_video=quote_or_video,
            author=request.user
        )
        return redirect('IDGenie:blog') # Redirect to the blog list page after posting
    
    return render(request, 'IDGenie/create_blog_post.html') # Render the blog creation form



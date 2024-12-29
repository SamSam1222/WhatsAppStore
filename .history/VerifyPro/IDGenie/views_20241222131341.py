from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost, Comment, Profile # Import your BlogPost model
from .forms import CommentForm
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User



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
    
    

@login_required
def get_user_avatar(request):
    avatar_url = request.user.profile.avatar.url if request.user.profile.avatar else "/path/to/default-avatar.png"
    return JsonResponse({"avatar_url": avatar_url})


# Login code

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to homepage or dashboard
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})




# SignUp Page

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the user
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create and save the profile
            profile = Profile(user=user)
            profile.avatar = form.cleaned_data.get('profile_picture')
            profile.save()

            # Login the user
            login(request, user)
            return redirect('index')  # Redirect to homepage or wherever you want
    else:
        form = SignUpForm()

    return render(request, 'IDGenie/signup.html', {'form': form})
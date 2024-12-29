from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost, Comment # Import your BlogPost model
from .forms import  CustomUserCreationForm
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# views.py

# Create your views here.
def index(request):
    # Fetch the welcoming page of the site
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/index.html', {'blog_posts': blog_posts})


def blogpost(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/blogpost.html', {'blog_posts': blog_posts})








# Login code

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('IDGenie:index')  # Redirect to home or dashboard page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'IDGenie/login.html', {'form': form})




def custom_logout(request):
    logout(request)
    return redirect('IDGenie:index')  # Redirect to login page after logging out


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Debugging: Check form validation success
            print("Form is valid!")  # Add this for debugging
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            messages.success(request, 'Your account has been created successfully!')
            return redirect('/')  # Redirect to the desired page (like home or dashboard)
        else:
            # Debugging: Check form errors
            print(form.errors)  # Add this to check form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            
            return render(request, 'IDGenie/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()  # Create an empty form for GET requests
    return render(request, 'IDGenie/signup.html', {'form': form})














# Handle comment thumbs-up and thumbs-down updates
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment, Vote
from django.contrib.auth.decorators import login_required

# This view is used to update the thumbs-up or thumbs-down vote
@login_required
@csrf_exempt
def update_vote(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        action = request.POST.get('action')

        try:
            # Get the comment object
            comment = Comment.objects.get(id=comment_id)
            user = request.user

            # Check if the user has already voted on this comment
            try:
                vote = Vote.objects.get(comment=comment, user=user)
                # If the user has voted, remove the previous vote
                if vote.action == action:
                    return JsonResponse({'error': 'You already voted for this action'}, status=400)
                else:
                    # Remove the previous vote count and update the vote
                    if vote.action == 'up':
                        comment.thumbs_up_count -= 1
                    elif vote.action == 'down':
                        comment.thumbs_down_count -= 1
                    
                    # Update the new vote
                    if action == 'up':
                        comment.thumbs_up_count += 1
                    elif action == 'down':
                        comment.thumbs_down_count += 1

                    # Save the updated comment and vote
                    vote.action = action
                    vote.save()
                    comment.save()

            except Vote.DoesNotExist:
                # If the user hasn't voted yet, add the vote
                if action == 'up':
                    comment.thumbs_up_count += 1
                elif action == 'down':
                    comment.thumbs_down_count += 1

                # Create a new vote record for this user
                Vote.objects.create(comment=comment, user=user, action=action)
                comment.save()

            # Return the updated thumbs count as JSON response
            return JsonResponse({
                'thumbs_up_count': comment.thumbs_up_count,
                'thumbs_down_count': comment.thumbs_down_count,
            })

        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Blog detail view where comments are added
def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    comments = blog_post.comments.all()  # Related comments
    images = blog_post.images.all()      # Related images

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            content = request.POST.get('content', '').strip()
            if content:
                comment = Comment.objects.create(
                    blog_post=blog_post,
                    author=request.user,
                    content=content
                )

                profile_picture_url = request.user.profile_picture.url if request.user.profile_picture else None

                return JsonResponse({
                    'id': comment.id,
                    'author': comment.author.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%B %d, %Y at %I:%M %p'),
                    'profile_picture_url': profile_picture_url,
                    'thumbs_up_count': comment.thumbs_up_count,
                    'thumbs_down_count': comment.thumbs_down_count,
                })
            return JsonResponse({'error': 'Comment content cannot be empty.'}, status=400)

        # Redirect unauthenticated user to login
        login_url = reverse('IDGenie:login')  # Replace 'login' with the name of your login view
        return JsonResponse({
            'error': 'User must be logged in to post comments.',
            'login_url': login_url
        }, status=403)

    form = CommentForm()

    return render(request, 'IDGenie/blog_detail.html', {
        'blog_post': blog_post,
        'comments': comments,
        'images': images,
        'form': form,
    })

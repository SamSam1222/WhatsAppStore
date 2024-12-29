from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.conf import settings  # For AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser

# CustomUser Model
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=20,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('P', 'Prefer not to say')],
        blank=True,
        null=True
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username

# BlogPost Model
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = RichTextField()  # CKEditor for rich text content
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# BlogPostImage Model (for additional images)
class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_extra_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.blog_post.title}"

# Comment Model
class Comment(models.Model):
    blog_post = models.ForeignKey(
        BlogPost, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )  # Links the comment to a blog post
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )  # The user who created the comment
    content = models.TextField()  # The content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the comment was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='replies'
    )  # Allows for replies to comments (self-referential)

    class Meta:
        ordering = ['-created_at']  # Orders comments by creation time in descending order

    def __str__(self):
        # Shows the author, content snippet, and parent status
        if self.parent:
            return f"Reply by {self.author.username} on {self.parent.author.username}'s comment"
        return f"Comment by {self.author.username} on {self.blog_post.title}"

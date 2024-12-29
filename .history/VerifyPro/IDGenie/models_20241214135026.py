from django.db import models
from django.contrib.auth.models import User # For author field
# Create your models here.


# BlogPost Model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() # Main content of the blog
    quote = models.TextField(blank=True, null=True) # Optional quote section
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True) # Optional image
    video_url = models.URLField(blank=True, null=True) # Optional video URL (for embedding)
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the post is created
    updated_at = models.DateTimeField(auto_now=True) # Timestamp when the post is last updated
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Author of the post
    
    def __str__(self):
        return self.title
    
    

# Comment Model for blog posts
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the post is created
    
    
    def __str__(self):
        return f"Comment by {self.author}"
    
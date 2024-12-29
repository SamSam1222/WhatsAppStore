from django.db import models
from django.contrib.auth.models import User # For author field
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255) # Title of the blog post
    content = models.TextField() # Content of the blog post
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True) # Blog image (optional)
    quote_or_video = models.TextField(blank=True, null=True) # Can store either a quote or a video embed code
    author = models.ForeignKey(User, on_delete=models.CASCADE) # To associate with the user who posted
    
    # Automatically order the blog posts by creation date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_recent_posts(self):
        """Method to fetch recent blog posts. """
        return BlogPost.objects.order_by('-created_at')[:5] # Adjust the number as needed
    
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.name} on {self.blog_post.title}"
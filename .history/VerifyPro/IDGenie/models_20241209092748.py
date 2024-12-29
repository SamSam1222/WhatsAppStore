from django.db import models
from django.contrib.auth.models import User # For author field
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255) # Title of the blog post
    content = models.TextField() # Content of the blog post
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True) # Blog image (optional)
    quote_or_video = models.TextField(blank=True, null=True) # Can store either a quote or a video embed code
    author = models.ForeignKey(User, on)
    
    # Automatically order the blog posts by creation date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at'] # Order by created_at in descending order, most recent first

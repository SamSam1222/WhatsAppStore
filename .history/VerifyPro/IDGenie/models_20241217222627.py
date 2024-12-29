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
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Author of the post
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the post is created
    updated_at = models.DateTimeField(auto_now=True) # Timestamp when the post is last updated
    
    def __str__(self):
        return self.title

# BlogParagraph Model
class BlogParagraph(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='paragraphs')
    content = models.TextField()
    
    def __str__(self):
        return f"Paragraph for {self.blog_post.title}"
    
# BlogPostImage Model (for additional images)
class BlogPostImage(models.Model):
    blog_post =models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_extra_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Image for {self.blog_post.title}"


# BlogQuote Model (for additional quotes)
class BlogQuote(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='quotes')
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Quote for {self.blog_post.title}"  
    
    

# Comment Model for blog posts
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # User who posted the comment
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog_post.title}"
    
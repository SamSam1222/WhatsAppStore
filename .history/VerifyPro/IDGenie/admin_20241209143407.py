from django.contrib import admin
from  .models import BlogPost, Comment
# Register your models here.


# BlogPost admin configuration
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at') # Display in the admin list view
    search_fields = ('title', 'content') # Searchable fields
    list_filter = ('created_at') # Filter by creation date
    
admin.site.register(BlogPost, BlogPostAdmin) # Register BlogPost model in admin
admin.site.register(Comment) # Register Comment model for the admin panel
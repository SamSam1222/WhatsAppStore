from django.contrib import admin
from .models import BlogPost, Comment
from .forms import BlogPostAdminForm


# BlogPost Admin
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm   # Use the custom form
    
    # Admin list view settings
    list_display = ('title', 'author', 'created_at', 'updated_at',)
    search_fields = ('title', 'content', 'author_username')         # Searchable fields
    list_filter = ('created_at', 'author')       # Filters on the right side
    
    
    # Organize fields in sections
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'content', 'quote', 'image', 'video_url', 'author'),
        }),
        ('Additional Options', {
            'fields': ('content_extra', 'image_extra', 'video_url_extra', 'quote_extra'),
            'classes': ('collapse',), # Makes this section collapsible
        }),
    )
    
    # Add more customization if needed (e.g., readonly fields, prepopulated fields)

# Registered BlogPost with custom admin
admin.site.register(BlogPost, BlogPostAdmin)


# Comment Admin (Simple)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog_post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'content')
    
admin.site.register(Comment, CommentAdmin)
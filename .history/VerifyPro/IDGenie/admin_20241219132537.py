from django.contrib import admin
from .models import BlogPost, BlogPostImage, Comment
from .forms import BlogPostAdminForm
from ckeditor.widgets import CKEditorWidget
from django import forms


# Inline for managing additional images
class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1  # Show 1 empty form for adding images by default


# Inline for managing comments
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Show 1 empty form for adding comments by default


# BlogPost Admin
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'updated_at', 'author')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from the title

    # Use inlines for managing additional images and comments
    inlines = [BlogPostImageInline, CommentInline]

    # Organize fields into sections
    fieldsets = (
        ('Main Info', {
            'fields': ('title', 'slug', 'content', 'image', 'video_url', 'author')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Make this section collapsible
        }),
    )
    readonly_fields = ('created_at', 'updated_at')  # Prevent editing dates

    # Define custom media for JavaScript and CSS
    class Media:
        js = (
            'static/ckeditor.js',  # Load CKEditor script
            'static/ckeditor_custom.js',  # Your custom JavaScript
        )
        css = {
            'all': ('static/ckeditor_custom.css',)  # Your custom CSS
        }


# Comment Admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'author', 'created_at', 'updated_at')
    search_fields = ('blog_post__title', 'author__username', 'content')
    list_filter = ('created_at', 'updated_at', 'author')
    readonly_fields = ('created_at', 'updated_at')  # Prevent editing dates


# Register models in the admin site
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)

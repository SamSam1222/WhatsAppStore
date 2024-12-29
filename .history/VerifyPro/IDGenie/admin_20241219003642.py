from django.contrib import admin
from .models import BlogPost, Comment
from .forms import BlogPostAdminForm

# BlogPost Admin
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')

    fieldsets = (
        ('Main Info', {
            'fields': ('title', 'content', 'quote', 'image', 'video_url', 'author')
        }),
        ('Additional Options', {
            'fields': ('content_extra', 'image_extra', 'image_extra2', 'video_url_extra', 'quote_extra', 'quote_extra2'),
            'classes': ('collapse',)
        }),
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog_post', 'created_at', 'content')
    search_fields = ('author__username', 'blog__post__title', 'content')
    list_filter = ('created_at',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)

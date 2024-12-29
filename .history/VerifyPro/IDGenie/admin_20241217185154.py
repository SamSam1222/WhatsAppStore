from django.contrib import admin
from .models import BlogPost
from .forms import BlogPostAdminForm

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')

admin.site.register(BlogPost, BlogPostAdmin)

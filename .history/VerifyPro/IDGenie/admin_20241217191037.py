from django.contrib import admin
from .models import BlogPost, BlogParagraph
from .forms import BlogPostAdminForm

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')
    
    
    class Media:
        js = ('js/admin_dynamic_fields.js',) # Load your custom JS file


class BlogParagraphInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = BlogParagraph
    extra = 1 # Start with 1 empty inline form

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    inlines = [BlogParagraphInline]

admin.site.register(BlogPost, BlogPostAdmin)

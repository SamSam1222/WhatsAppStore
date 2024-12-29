from django.contrib import admin
from  .models import BlogPost, Comment
# Register your models here.

# BlogPost Admin Form
class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        field = ['title', 'content', 'quote', 'image', 'video_url', 'author']
        
    # Additional fields for adding paragraphs dynamically
    content_extra = forms.CharField(widget=forms.Textarea, required=False, label="Addition Paragraph")
    image_extra = forms.ImageField(required=False, lable="Additional Image")
    video_url_extra = forms.URLField(required=False, label="Additional Video URL")
    quote_extra = forms.CharField(widget=forms.Textarea, required=False, label="Quote", help_text="This is optional.")
    
    
    # Override save method to include additional paragraphs, images, etc.
    def save(self, commit=True):
        blog_post = super().save(commit=False)
        
        
        # Handle the additional content and media fields here
        if commit:
            blog_post.save()
            
        # Optionally, handle additional paragraphs, images, and videos here
        
        return blog_post
    
# BlogPostAdmin(admin.ModelAdmin):
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at')
    
    fieldsets = (
        ('Main Info', {
            'fields': ('title', 'content', 'quote', 'image', 'video_url', 'author')  
        }),
        ('Additional Options', {
            'fields': ('content_extra', 'image_extra', 'video_url_extra', 'quote_extra'),
            'classes': ('collapse',)
        }),
    )
    
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
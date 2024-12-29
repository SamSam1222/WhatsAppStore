from django import forms 
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    # Custom additional fields
    content_extra = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add another paragraph...'}),
        required=False,
        label="Additional Paragraph"
    )
    image_extra = forms.ImageField(required=False, label="Additional Image")
    video_url_extra = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder': 'Paste video URL here...'}),
        required=False,
        label="Additional Video URL"
    )
    quote_extra = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Add a quote...'}),
        required=False,
        label="Quote"
    )
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'quote', 'image', 'video_url', 'author']
    
    def save(self, commit=True):
        blog_post = super().save(commit=False)
        # Append additional paragraph to the main content if provided
        content_extra = self.cleaned_data.get('content_extra')
        if content_extra:
            blog_post.content += f"\n\n{'content_extra'}"
        
        # Handle extra media (image and video) logic here if needed
        # For now, we are only saving the main image and video fields
        
        if commit:
            blog_post.save()
        return blog_post
from django import forms 
from .models import BlogPost


class BlogPostAdminForm(forms.ModelForm):
    # Additional fields for dynamics content
    content_extra = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        required=False,
        label="Additional Paragraph"
    )
    image_extra = forms.ImageField(required=False, label="Additional Image")
    video_url_extra = forms.URLField(required=False, label="Additional Video URL")
    quote_extra = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2, "cols": 40}),
        required=False,
        label="Optional Quote"
    )
    
 
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'quote', 'image', 'video_url', 'author']
        
        
    # Custom save method to handle extra fields
    def save(self, commit=True):
        blog_post = super().save(commit=False)
        
        # Append extra content to the existing content
        content_extra = self.cleaned_data.get('content_extra')
        if content_extra:
            blog_post.content += f"\n\n{content_extra}"
        
        
        # Add extra quote to the content
        quote_extra = self.cleaned_data.get('quote_extra')
        if quote_extra:
            blog_post.content += f"\n\n---\nQuote: {quote_extra}\n---"
            
        # Save image and video URLs as needed (optional handling)
        # This part can be expanded to save into related models
        
        if commit:
            blog_post.save()
        return blog_post
from django import forms
from .models import BlogPost, BlogParagraph, BlogPostImage


class BlogPostAdminForm(forms.ModelForm):
    # Additional fields for dynamic content and media
    content_extra = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        required=False,
        label="Additional Paragraph"
    )
    image_extra = forms.ImageField(required=False, label="Additional Image 1")
    image_extra2 = forms.ImageField(required=False, label="Additional Image 2")
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
        
        # Append additional content
        content_extra = self.cleaned_data.get('content_extra')
        if content_extra:
            BlogParagraph.objects.create(blog_post=blog_post, content=content_extra)
        
        # Append optional quote
        quote_extra = self.cleaned_data.get('quote_extra')
        if quote_extra:
            BlogParagraph.objects.create(blog_post=blog_post, content=f"Quote: {quote_extra}")

        if commit:
            blog_post.save()

        # Handle additional images
        image_extra = self.cleaned_data.get('image_extra')
        image_extra2 = self.cleaned_data.get('image_extra2')
        
        if image_extra:
            BlogPostImage.objects.create(blog_post=blog_post, image=image_extra)
        if image_extra2:
            BlogPostImage.objects.create(blog_post=blog_post, image=image_extra2)

        return blog_post

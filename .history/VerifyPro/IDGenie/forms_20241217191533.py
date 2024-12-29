from django import forms
from .models import BlogPost


class BlogPostAdminForm(forms.ModelForm):
    # Additional dynamic fields for content and media
    content_extra = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        required=False,
        label="Additional Paragraph"
    )
    image_extra = forms.ImageField(required=False, label="Additional Image 1")
    image_extra2 = forms.ImageField(required=False, label="Additional Image 2")
    image_extra3 = forms.ImageField(required=False, label="Additional Image 3")
    video_url_extra = forms.URLField(
        required=False, label="Additional Video URL"
    )
    quote_extra = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2, "cols": 40}),
        required=False,
        label="Optional Quote"
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'quote', 'image', 'video_url', 'author']

    # Custom save method to append dynamic fields
    def save(self, commit=True):
        blog_post = super().save(commit=False)
        
        # Append additional content to the existing content
        content_extra = self.cleaned_data.get('content_extra')
        if content_extra:
            blog_post.content += f"\n\n{content_extra}"
        
        # Append optional quote to content
        quote_extra = self.cleaned_data.get('quote_extra')
        if quote_extra:
            blog_post.content += f"\n\n---\nQuote: {quote_extra}\n---"

        # Save the main form first
        if commit:
            blog_post.save()

        # Handle additional images
        image_extra = self.cleaned_data.get('image_extra')
        image_extra2 = self.cleaned_data.get('image_extra2')
        image_extra3 = self.cleaned_data.get('image_extra3')

        # Save extra images as needed
        if image_extra:
            BlogPostImage.objects.create(blog_post=blog_post, image=image_extra)
        if image_extra2:
            BlogPostImage.objects.create(blog_post=blog_post, image=image_extra2)
        if image_extra3:
            BlogPostImage.objects.create(blog_post=blog_post, image=image_extra3)
        
        return blog_post

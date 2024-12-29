from django import forms
from .models import BlogPost


class BlogPostAdminForm(forms.ModelForm):
    # Additional fields for dynamic content
    content_extra = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        required=False,
        label="Additional Paragraph"
    )
    image_extra = forms.ImageField(required=False, label="Additional Image")
    video_url_extra = forms.URLField(
        required=False, label="Additional Video URL",
        help_text="Paste the video URL here (e.g., YouTube, Vimeo)."
    )
    quote_extra = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2, "cols": 40}),
        required=False,
        label="Optional Quote",
        help_text="Add an optional quote to highlight."
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'quote', 'image', 'video_url', 'author']

    # Custom save method to handle the extra fields
    def save(self, commit=True):
        blog_post = super().save(commit=False)

        # Append additional paragraph to the existing content
        content_extra = self.cleaned_data.get('content_extra')
        if content_extra:
            blog_post.content += f"\n\n{content_extra}"

        # Append additional quote if provided
        quote_extra = self.cleaned_data.get('quote_extra')
        if quote_extra:
            blog_post.content += f"\n\n---\nQuote: {quote_extra}\n---"

        # Handle additional image (optional)
        image_extra = self.cleaned_data.get('image_extra')
        if image_extra:
            # You can save the extra image to a related model or process it here
            # For now, appending a placeholder text to content
            blog_post.content += f"\n\n[Additional Image Added]"

        # Handle additional video URL (optional)
        video_url_extra = self.cleaned_data.get('video_url_extra')
        if video_url_extra:
            blog_post.content += f"\n\nVideo: {video_url_extra}"

        if commit:
            blog_post.save()

        return blog_post

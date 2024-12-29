from django import forms
from .models import BlogPost, BlogParagraph, BlogPostImage, BlogQuote, Comment


class BlogPostAdminForm(forms.ModelForm):
    # Fields for dynamic content
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
        label="Additional Quote 1"
    )
    quote_extra2 = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2, "cols": 40}),
        required=False,
        label="Additional Quote 2"
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'quote', 'image', 'video_url', 'author']

    # Custom save method to handle extra fields
    def save(self, commit=True):
        blog_post = super().save(commit=False)

        # Append additional paragraphs
        content_extra = self.cleaned_data.get('content_extra')
        if content_extra:
            BlogParagraph.objects.create(blog_post=blog_post, content=content_extra)

        # Append additional quotes
        quote_extra = self.cleaned_data.get('quote_extra')
        quote_extra2 = self.cleaned_data.get('quote_extra2')
        if quote_extra:
            BlogQuote.objects.create(blog_post=blog_post, quote=quote_extra)
        if quote_extra2:
            BlogQuote.objects.create(blog_post=blog_post, quote=quote_extra2)

        # Save additional images
        if commit:
            blog_post.save()

        image_extra = self.cleaned_data.get('image_extra')
        image_extra2 = self.cleaned_data.get('image_extra2')
        if image_extra:
            BlogPostImage.objects.create(blog_post=blog_post, image=image_extra)
        if image_extra2:
            BlogPostImage.objects.create(blog_post=blog_post, image=image_extra2)

        return blog_post
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
            
        }

from django import forms
from .models import BlogPost, BlogParagraph, BlogPostImage, BlogQuote, Comment



class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'quote', 'image', 'video_url', 'author']

    # Custom save method to handle extra fields (like saving images or video URLs)
    def save(self, commit=True):
        blog_post = super().save(commit=False)

        # If any additional processing for rich content or media is needed, handle it here

        if commit:
            blog_post.save()

        return blog_post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }

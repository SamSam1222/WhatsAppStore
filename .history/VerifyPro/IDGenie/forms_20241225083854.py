from django import forms
from .models import BlogPost, Comment
from ckeditor.widgets import CKEditorWidget  # Import CKEditorWidget
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Form for handling BlogPost in the Admin interface
# forms.py
from .models import CustomUser

class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'video_url', 'author']  # 'quote' removed since CKEditor handles rich content
        widgets = {
            'content': CKEditorWidget(),  # Using CKEditor for the content field
        }

    # Custom save method to handle extra fields (if needed)
    def save(self, commit=True):
        blog_post = super().save(commit=False)

        # Any additional processing for media (like saving images or video URLs) can go here
        if commit:
            blog_post.save()

        return blog_post


# Form for handling Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )  
    


class CustomUserCreationForm(UserCreationForm):
    # Custom fields for first name, last name, etc.
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say')
    ]
    gender = forms.ChoiceField(choices=gender_choices, required=True, label="Gender", initial='P')
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
    profile_picture = forms.ImageField(required=False, label="Profile Picture")

    # Remove password2 from the form
    password2 = None  # Explicitly remove password2

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone_number', 'profile_picture', 'username', 'password1']

    # Override clean method to avoid password2 validation
    def clean(self):
        cleaned_data = super().clean()
        # Ensure password2 is not in the cleaned data and not validated
        if 'password2' in cleaned_data:
            del cleaned_data['password2']
        return cleaned_data
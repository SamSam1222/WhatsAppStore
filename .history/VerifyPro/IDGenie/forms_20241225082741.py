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
    # Additional fields for first name, last name, gender, phone number, and profile picture
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    
    # Gender field with choices for Male, Female, Other, and Prefer not to say
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say')
    ]
    gender = forms.ChoiceField(choices=gender_choices, required=True, label="Gender", initial='P')
    
    # Optional fields for phone number and profile picture
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
    profile_picture = forms.ImageField(required=False, label="Profile Picture")

    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'gender', 
            'phone_number', 
            'profile_picture', 
            'username', 
            'password'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.gender = self.cleaned_data.get('gender')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.profile_picture = self.cleaned_data.get('profile_picture')
        
        # Set the password to the `password` field since we are using only one password field
        user.set_password(self.cleaned_data.get('password'))
        
        if commit:
            user.save()
        return user

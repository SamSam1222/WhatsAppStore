from django.contrib import admin
from .models import BlogPost, BlogPostImage, Comment, Profile, CustomUser
from .forms import BlogPostAdminForm
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin

# Inline for managing additional images
class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1  # Show 1 empty form for adding images by default


# Inline for managing comments
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Show 1 empty form for adding comments by default


# BlogPost Admin
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'updated_at', 'author')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from the title

    # Use inlines for managing additional images and comments
    inlines = [BlogPostImageInline, CommentInline]

    # Organize fields into sections
    fieldsets = (
        ('Main Info', {
            'fields': ('title', 'slug', 'content', 'image', 'video_url', 'author')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Make this section collapsible
        }),
    )
    readonly_fields = ('created_at', 'updated_at')  # Prevent editing dates


# Comment Admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'author', 'created_at', 'updated_at')
    search_fields = ('blog_post__title', 'author__username', 'content')
    list_filter = ('created_at', 'updated_at', 'author')
    readonly_fields = ('created_at', 'updated_at')  # Prevent editing dates

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar_display']  # Add avatar_display to list_display

    def avatar_display(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.avatar.url)
        return "No Avatar"
    avatar_display.short_description = 'Avatar'  # Set the column name in the admin interface
    
# Register models in the admin site




class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'profile_picture', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.unregister(Profile)  # Unregister if already registered
admin.site.register(Profile, ProfileAdmin)  # Re-register with the updated class

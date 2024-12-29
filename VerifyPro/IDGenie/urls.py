from django.urls import path, include
# from IDGenie.views import index, blog
from .import views
from .views import login_view, signup_view, custom_logout

app_name ="IDGenie"

urlpatterns = [
    
    # HomePage URL  
    path('', views.index, name='index'),
    
    path('update-thumbs/', views.update_thumbs, name='update_thumbs'),

    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'), # BLog detail View
    
    #Blog Post URL
    path('blog/', views.blogpost, name='blog_list'), # BLog List View
    
    
    # path('create/', views.create_blog_post, name='create_blog_post'), # Blog create view  
    
  
    
    # Login url
    path('login/', login_view, name='login'),
    
    # Login Out URL
    path('logout/', custom_logout, name='logout'),
    
    # SignUp Url
    path('signup/', signup_view, name='signup'),
    

]

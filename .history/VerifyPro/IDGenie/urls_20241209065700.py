from django.urls import path, include
# from IDGenie.views import index, blog
from . import views

app_name ="IDGenie"

urlpatterns = [
    
    # HomePage URL  
    path('', views.index, name='index'),
    
    #Blog Post URL
    path('blog/', views.blogpost, name='blog'), # BLog List View
    
    
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'), # BLog detail View
    
    
    
]

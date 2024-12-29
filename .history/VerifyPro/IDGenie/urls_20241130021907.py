from django.urls import path, include
from IDGenie.views import index, blogpost_view
from . import views
app_name ="IDGenie"

urlpatterns = [
    
    # HomePage URL  
    path('', index, name = 'index'),
    
    #Blog Post URL
    path('blogpost/', blogpost_view, name = 'blogpost'),
    
    
]

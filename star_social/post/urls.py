from django.contrib import admin
from django.urls import path
from .views import ListUserPosts, CreatePost

app_name='post'

urlpatterns = [
    path('by/<slug:user>', ListUserPosts.as_view(), name="list_posts"),
    path('new/', CreatePost.as_view(), name="create_post"),
    
]
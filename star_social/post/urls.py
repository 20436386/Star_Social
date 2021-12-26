from django.contrib import admin
from django.urls import path
from .views import ListUserPosts, CreatePost, PostDetailView, PostDeleteView

app_name='post'

urlpatterns = [
    path('by/<slug:user>', ListUserPosts.as_view(), name="list_posts"),
    path('new/', CreatePost.as_view(), name="create_post"),
    path('by/<slug:user>/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('by/<slug:user>/<int:pk>/remove', PostDeleteView.as_view(), name="post_delete"),

    
]
from django.contrib import admin
from django.urls import path, include
from .views import CreateGroup

app_name = "group"

urlpatterns = [
    path('new/', CreateGroup.as_view(), name="create_group"),
]

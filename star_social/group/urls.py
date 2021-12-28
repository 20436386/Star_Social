from django.contrib import admin
from django.urls import path, include
from .views import CreateGroupView, GroupListView, GroupDetailView, JoinGroup, LeaveGroup

app_name = "group"

urlpatterns = [
    path('new/', CreateGroupView.as_view(), name="create_group"),
    path('', GroupListView.as_view(), name="list_group"),
    path('<slug>', GroupDetailView.as_view(), name="group_detail"),
    path('member/add/<slug>', JoinGroup.as_view(), name="add_member"),
    path('member/remove/<slug>', LeaveGroup.as_view(), name="remove_member"),

]

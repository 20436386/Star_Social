from django.contrib import admin
from django.urls import path, include
from .views import CreateGroupView, GroupListView, GroupDetailView, group_member_add, group_member_remove

app_name = "group"

urlpatterns = [
    path('new/', CreateGroupView.as_view(), name="create_group"),
    path('list/', GroupListView.as_view(), name="list_group"),
    path('detail/<int:pk>', GroupDetailView.as_view(), name="group_detail"),
    path('member/add/<int:pk>', group_member_add, name="add_member"),
    path('member/remove/<int:pk>', group_member_remove, name="remove_member"),

]

from django.contrib import admin
from.models import Post


class PostAdmin(admin.ModelAdmin):
    # Alter order of fields to alter order displayed on admin page
    fields = ['user', 'group', 'content', 'create_date']
    # Include all parameters that you would like to be able to search for
    search_fields=['group']
    # This list adds filters to the side
    list_filter=['user', 'group', 'create_date']
    # This list will display parameters on list page, note cant be manytomanyfield
    list_display=['user', 'group', 'content', 'create_date']
    # This list will allow you to edit fields on list page
    list_editable=['group']


# Register your models here.
admin.site.register(Post, PostAdmin)
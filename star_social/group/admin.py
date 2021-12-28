from django.contrib import admin
from.models import Group

class GroupAdmin(admin.ModelAdmin):
    # Alter order of fields to alter order displayed on admin page
    fields = ['name', 'slug', 'description', 'users']
    # Include all parameters that you would like to be able to search for
    search_fields=['name']
    # This list adds filters to the side
    list_filter=['users']
    # This list will display parameters on list page, note cant be manytomanyfield
    list_display=['name', 'description']
    # This list will allow you to edit fields on list page
    list_editable=['description']

# Register your models here.
admin.site.register(Group, GroupAdmin)

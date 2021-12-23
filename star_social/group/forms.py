from django import forms
from django.db.models import fields
from django.forms import forms
from .models import Group

class GroupForm(forms.Form):
    
    class Meta():
        model = Group
        fields = "__all__"
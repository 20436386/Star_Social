from django import forms
from django.db.models import fields
from .models import Group
from django.utils.translation import gettext_lazy as _

class GroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        exclude = ['users']

        labels = {
                'name': _('Name'),
            }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

    # https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/
    # widgets = {
    #         'name': forms.Textarea(attrs={'placeholder':'name'}),
    #     }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #The style attribute should be placed in css file
        self.fields['name'].widget.attrs.update({'class': 'text_input', 'placeholder':'Name'})
        self.fields['description'].widget.attrs.update({'class': 'text_input','placeholder':'Description'})

    

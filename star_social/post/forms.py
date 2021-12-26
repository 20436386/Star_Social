from django import forms
from django.db.models import fields
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content','group')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #The style attribute should be placed in css file
        self.fields['content'].widget.attrs.update({'class': 'text_input', 'placeholder':'Post Content'})
        self.fields['group'].widget.attrs.update({'class': 'text_input'})

    


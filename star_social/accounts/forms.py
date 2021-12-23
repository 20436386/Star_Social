from django.forms import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This form extends UserCreationForm to include email field
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms
class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

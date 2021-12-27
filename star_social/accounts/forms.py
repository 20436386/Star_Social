from django.forms import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# This form extends UserCreationForm to include email field
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms
class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #The style attribute should be placed in css file
        self.fields['username'].widget.attrs.update({'class': 'text_input','placeholder':'username'})
        self.fields['username'].label = 'Display Name'
        self.fields['email'].widget.attrs.update({'class': 'text_input','placeholder':'someone@gmail.com'})
        # /home/phoenix/python_env/myDjango/lib/python3.9/site-packages/django/contrib/auth/forms.py
        self.fields['password1'].widget.attrs.update({'class': 'text_input','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'text_input','placeholder':'Password'})

# https://www.notimedad.dev/customizing-django-builtin-login-form/
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'text_input','placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class': 'text_input','placeholder':'Password'})

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import CreateUser
from .forms import CustomAuthenticationForm

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'), #The template_name provided here is the html to be displayed after logout has occurred
    # Include other auth_views here 
    path('accounts/register/', CreateUser.as_view(), name='register'),

]

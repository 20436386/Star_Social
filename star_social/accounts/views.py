from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#formview
class CreateUser(FormView):
    template_name = "accounts/registration.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form) -> HttpResponse:
        # https://docs.djangoproject.com/en/4.0/ref/forms/api/
        email = form.cleaned_data['email']
        new_user = form.save(commit=False)
        new_user.email = email
        new_user.save()
        return super().form_valid(form)
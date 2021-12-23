from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DeleteView, CreateView, DetailView, UpdateView)
from django.views.generic.edit import FormView
from .models import Post
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GroupForm
from django.urls import reverse_lazy

class CreateGroup(FormView):
    template_name = 'group/create_group.html'
    form_class = GroupForm
    # success_url = reverse_lazy("")

    # def form_valid(self, form):
    #     return super().form_valid(form)

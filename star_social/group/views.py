from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import (TemplateView, ListView, DeleteView, CreateView, DetailView, UpdateView)
from django.views.generic.edit import FormView
from .models import Group
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GroupForm
from django.urls import reverse_lazy

class CreateGroupView(LoginRequiredMixin, CreateView):
    login = 'accounts/login.html'

    template_name = 'group/create_group.html'
    form_class = GroupForm
    model = Group
    # success_url = reverse_lazy("")

    def form_valid(self, form):
        form = self.get_form()
        group_object = form.save()
        group_object.users.add(self.request.user)
        return super().form_valid(form)

class GroupListView(ListView):
    
    model=Group
    template_name = 'group/group_list.html'

    # def get_queryset(self):
    #     return super().get_queryset()

class GroupDetailView(DeleteView):

    model=Group
    template_name = 'group/group_detail.html'

def group_member_add(request, pk):
    group_object = Group.objects.get(pk=pk)
    print(group_object)
    group_object.users.add(request.user)
    group_object.save()
    print(group_object.pk)
    return HttpResponseRedirect(reverse("group:group_detail", kwargs={'pk':group_object.pk}))

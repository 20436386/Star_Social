from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import (TemplateView, ListView, DeleteView, CreateView, DetailView, UpdateView, RedirectView)
from django.views.generic.edit import FormView
from .models import Group
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GroupForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

class GroupDetailView(DetailView):

    model=Group
    template_name = 'group/group_detail.html'

    # NOTE: Dont need this as it can be done in template itself using {% if user in group.users.all %}
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_user = self.request.user
    #     current_group = self.get_object()
    #     if current_user in current_group.users.all():
    #         context['is_member'] = True
    #     else:
    #         context['is_member'] = False
    #     return context

class JoinGroup(LoginRequiredMixin, RedirectView):
    login = 'accounts/login.html'

    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:group_detail', kwargs={'slug': kwargs['slug']})

    def get(self, request, *args, **kwargs):
        try:
            group_object = Group.objects.get(slug=kwargs['slug'])
        except:
            # To display messages, need to include relevant template tags in templates.
            messages.warning(self.request,"Warning, you are already a member of this group")
        else:
            group_object.users.add(request.user)
            group_object.save()
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):
    login = 'accounts/login.html'

    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:group_detail', kwargs={'slug': kwargs['slug']})

    def get(self, request, *args, **kwargs):
        try:
            group_object = Group.objects.get(slug=kwargs['slug'])
        except:
            messages.warning(self.request,"Warning, you are not a member of this group")
        else:
            group_object.users.remove(request.user)
            group_object.save()
        return super().get(request, *args, **kwargs)
        
# @login_required
# def group_member_add(request, slug):
#     # print("group add")
#     group_object = Group.objects.get(slug=slug)
#     # print(group_object)
#     group_object.users.add(request.user)
#     group_object.save()
#     # print(group_object.users.all())
#     return HttpResponseRedirect(reverse("group:group_detail", kwargs={'slug':group_object.slug}))

# @login_required
# def group_member_remove(request, slug):
#     # print("group remove")
#     group_object = Group.objects.get(slug=slug)
#     # print(group_object)
#     group_object.users.remove(request.user)
#     group_object.save()
#     # print(group_object.users.all())
#     return HttpResponseRedirect(reverse("group:group_detail", kwargs={'slug':group_object.slug}))
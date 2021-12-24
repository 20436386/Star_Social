from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DeleteView, CreateView, DetailView, UpdateView)
from .models import Post
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class ListUserPosts(ListView):

    model = Post
    template_name = 'post/post_list.html'


    def get_queryset(self):
        # if self.request.user.is_authenticated():
        #     return Post.objects.filter(user=self.request.user)
        # else:
        #     return Post.objects.filter(user=self.kwargs['user'])
        user = User.objects.get(username=self.kwargs['user'])
        return Post.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug_user'] = self.kwargs['user']
        return context
        

class CreatePost(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'

    model=Post
    template_name = 'post/create_post.html'

    fields = ('content','group')

    def form_valid(self, form):
        user = self.request.user
        print(user)
        new_post = form.save(commit=False)
        new_post.user = user
        new_post.create_date = timezone.now()
        new_post.save()
        print("user={}\ncontent={}\ncreate_date={}".format(new_post.user, new_post.content, new_post.create_date))
        return super().form_valid(form)
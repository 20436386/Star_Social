from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from group.models import Group
from django.contrib.auth import get_user, get_user_model

import misaka

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(max_length=512)
    content_html = models.TextField(max_length=512)
    # The auto_now parameter will automatically fill in the current datetime value. For some reason create_date field does not show in admin page, although the value is known to django
    create_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post:list_posts", kwargs={"user": self.user})

    def save(self, *args, **kwargs):
        self.content_html = misaka.html(self.content)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "{}, created on {}".format(self.user, self.create_date)

    class Meta:
        ordering = ["-create_date"]
        # In SQL equivalent to making a pair of fields the primary key
        unique_together = ['user', 'content']
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=512)
    # Will use this in group detail view, must have button that will add user to the current group
    users = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse("group:group_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    


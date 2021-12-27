from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
# This method replaces spaces with hyphens and lowercases strings
from django.utils.text import slugify

# This python library allows people to write markdown in the description
import misaka

# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#extending-the-existing-user-model
# https://stackoverflow.com/questions/45499641/django-custom-user-model-best-practice-user-get-user-model
# This function returns the currently active user model i.e. the custom one. Refer to above links on creating custom user model - it is recommended apparently
User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(max_length=512, blank=True, default='')
    description_html = models.TextField(max_length=512, editable=False, blank=True, default='')
    # Will use this in group detail view, must have button that will add user to the current group
    # Check part six here
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("group:group_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]

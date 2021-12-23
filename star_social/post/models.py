from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from group.models import Group

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(max_length=512)
    create_date = models.DateTimeField()

    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse("post:list_posts", kwargs={"user": self.user})

    def __str__(self) -> str:
        return "{}, created on {}".format(self.user, self.create_date)
from django.db import models
from post.models import Post

class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=512)

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    


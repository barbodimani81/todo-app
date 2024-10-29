from django.db import models
from django.urls import reverse


class Task(models.Model):
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_relative_url(self):
        return reverse("todo:task-detail", kwargs={"pk": self.pk})


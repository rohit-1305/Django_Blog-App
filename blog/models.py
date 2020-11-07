from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    aurthor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # after creating the post it should return the url as a string
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
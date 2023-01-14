from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author title text created_date published_date
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)  # Modified by learner[me].
    updated_date = models.DateTimeField(auto_now=True)  # Added by learner[me].
    # created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

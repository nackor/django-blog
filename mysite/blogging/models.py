from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    author = models.CharField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
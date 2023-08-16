from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    author = models.CharField(default=0)
    created_date 
    modified_date
    published_date

    def __str__(self):
        return self.title
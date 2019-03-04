from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BloggerModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    blog_title = models.CharField(max_length=50)
    blog_entry = models.TextField(max_length=10000)

    def __str__(self):
        return self.blog_title

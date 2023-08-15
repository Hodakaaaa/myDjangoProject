# models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set a default user

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

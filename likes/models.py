from calendar import c
from turtle import title
from django.db import models

from django.contrib.auth.models import User
from posts.models import Post 



class Like(models.Model):
    """Like model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)

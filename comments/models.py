from django.db import models
from django.contrib.auth.models import User
from posts.models import Post 



class Comment(models.Model):
    """Comment model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    
    content = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

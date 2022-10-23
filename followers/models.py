from django.db import models

from django.contrib.auth.models import User



class Follower(models.Model):
    """Follower model."""
    user = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='follower',on_delete=models.CASCADE)
    #user = models.ManyToManyField(User)
    accepted =models.BooleanField(default=True)

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from followers.models import Follower

@login_required
def follow (request,follower):
    user = request.user
    follower = User.objects.get(username=follower)
    try:
        following= Follower.objects.get(user=user, follower=follower)
        following.delete()
        
    except Follower.DoesNotExist:
        p=Follower.objects.create(user=user,follower=follower,accepted=False)
        
    return redirect('Detail',username= follower)
    
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from .models import Like
from users.models import User


@login_required
def like (request,post_id):
    user = request.user
    user = User.objects.get(username=user)
    post = Post.objects.get(id=post_id)
    
    try:
        like = Like.objects.get(user=user,post=post)
        like.delete()
        post.likes=post.likes-1
        post.save()
        
    except Like.DoesNotExist:
        p=Like.objects.create(user=user,post=post,profile=user.profile)
        post.likes=post.likes+1
        post.save()
        
    return redirect('feed')
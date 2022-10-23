from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Comment
from .models import Post

@login_required
def add_comment(request,post_id):
    try:
        post = Post.objects.get(id=post_id)
        if request.method == 'POST':
            if request.POST.get("comment"):
                comment=Comment.objects.create(user=request.user, 
                                            profile=request.user.profile,
                                            post=post,
                                            content=request.POST.get("comment"))
                return redirect('post_detail', post_id)
    except Post.DoesNotExist:
        return redirect('feed')
    return render(request,'comments/new.html',{'post': post})


@login_required
def delete_comment(request,comment_id):
    
    try:
        comment = Comment.objects.get(id=comment_id, user=request.user)
        post_id= comment.post_id
        comment.delete()
        return redirect('post_detail', post_id)
    except Post.DoesNotExist:
        return redirect('feed')


@login_required
def update_comment(request,comment_id):
    
    try:
        comment = Comment.objects.get(id=comment_id, user=request.user)
        if request.method == 'POST':
            if request.POST.get("comment"):
                
                comment.content=request.POST.get("comment")
                comment.save()
                return redirect('post_detail', comment.post_id)
            else:
                return render(request,'comments/new.html',{'post': comment.post})
        else:
                return render(request,'comments/new.html',{'post': comment.post})
    except Comment.DoesNotExist:
            return redirect('feed')
    
    
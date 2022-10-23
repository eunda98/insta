from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Forms
from .forms import PostForm,updatePostForm
# Models
from posts.models import Post
from comments.models import Comment
from django.views.decorators.csrf import csrf_exempt


def list_posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request,'posts/new.html',{'form': form,'user': request.user,'profile': request.user.profile
        }
    )

@login_required
def update_post(request, post_id):
    if request.method == 'POST':
        form = updatePostForm(request.POST, request.FILES)
        try:
            post = Post.objects.get(id=post_id, user=request.user)
            if form.is_valid():
                data = form.cleaned_data
                post.title = data['title']
                post.photo = data['photo']
                post.save()
                messages.success(request, "saved successfully") 
                return redirect('feed')
        except Post.DoesNotExist:
            messages.error(request, "There was an error saving")        
    else:
        form = PostForm()
    return render(request,'posts/new.html',{'form': form,'user': request.user,'profile': request.user.profile})

@login_required
def delete_post(request, post_id):     
    try:
        post = Post.objects.get(id=post_id,user=request.user) 
        post.delete()
        return redirect('feed')
    except Post.DoesNotExist:
        return redirect('feed', {'error': 'the post does not exist'})

def detail_post(request,post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments= Comment.objects.filter(post=post)
        return render(request,'posts/detail.html',{'post':post,'comments':comments})

    except Post.DoesNotExist:
        return redirect('feed')


    

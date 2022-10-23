from bson import is_valid
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post
from followers.models import Follower

#@csrf_exempt
from django.views.decorators.csrf import csrf_exempt

# Forms
from users.forms import ProfileForm, SignupForm

def detail(request,username):
    try:
        user = User.objects.get(username=username)    
        posts= Post.objects.filter(user=user).order_by('-created')
        following = Follower.objects.filter(user=user)
        followers= Follower.objects.filter(follower=user)
        if  not request.user.is_anonymous:
            unfollow= Follower.objects.filter(follower=user,user=request.user).exists()
        else:
           unfollow=False 

    except User.DoesNotExist:  
        user=None
        posts=[]
        followers=[]
        following=[]
        unfollow=False
    return render(request, 'users/detail.html', {'user': user, 'posts':posts,'post':posts.__len__,
                'followers':followers.__len__,
                'following':following.__len__,
                'unfollow':unfollow})


@login_required
def update_profile(request):

    profile = request.user.profile
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('Detail',username= profile.user.username)

    return render(request,'users/update_profile.html',{'profile': profile,'user': request.user,'form': form})


@login_required
def delete_user(request):

    try:
        user = User.objects.get(username=request.user)
        user.delete()
        return redirect('login')
    except User.DoesNotExist:
        return redirect('feed')     
        

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def signup(request):
    form = SignupForm()  
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'users/signup.html',{'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
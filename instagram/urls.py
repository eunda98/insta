"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
#from . import views
from django.conf import settings
from django.conf.urls.static import static
from posts import views_post
from users import users_views
from followers import views
from likes import likes_views
from comments import c_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hi/',views.hi),
    
    path('', views_post.list_posts, name='feed'),
    path('posts/update/<int:post_id>', views_post.update_post, name='update_post'),
    path('posts/new/', views_post.create_post, name='create_post'),
    path('posts/delete/<int:post_id>', views_post.delete_post, name='delete_post'),
    path('post/detail/<int:post_id>',views_post.detail_post,name='post_detail'),

    path('users/login/', users_views.login_view,name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/detail/<str:username>/', users_views.detail, name='Detail'),
    path('users/delete/', users_views.delete_user, name='Delete'),
    path('users/update/', users_views.update_profile, name='update_profile'),

    path('follower/<str:follower>/',views.follow,name='follow'),
    
    path('like/<int:post_id>/',likes_views.like,name='like'),

    path('comments/add/<int:post_id>/',c_views.add_comment,name='comments_add'),
    path('comments/update/<int:comment_id>/',c_views.update_comment,name='comments_update'),
    path('comments/delete/<int:comment_id>/',c_views.delete_comment,name='comments_delete'),

    path('accounts/', include('django.contrib.auth.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




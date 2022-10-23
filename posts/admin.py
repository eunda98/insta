from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class ProfilAdmin(admin.ModelAdmin):
    list_display=('pk','user','title','photo','likes')
    search_fields=(
        'pk',
        'user',
        'title',
        'photo'
            )
    list_filter=('created','modified')

from django.contrib import admin
from .models import Follower

@admin.register(Follower)
class followerAdmin(admin.ModelAdmin):
    list_display=('pk','user','follower')
    search_fields=(
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
            )



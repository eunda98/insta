from django.contrib import admin
from .models import Like

@admin.register(Like)
class likesAdmin(admin.ModelAdmin):
    list_display=('pk','user','profile_id','post_id')
    search_fields=(
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
            )


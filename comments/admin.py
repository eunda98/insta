from django.contrib import admin

from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('pk','user','post_id','content', 'created')
    search_fields=(
        'user__email',
        'user__first_name',
        'user__last_name',
            )
    list_filter=('created','modified')


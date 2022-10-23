from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class ProfilAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone_number','picture','website', 'created','modified')
    #list_display_links=('user','phone_number','picture', 'created','modified')
    list_editable=('phone_number','picture')
    search_fields=(
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
            )
    list_filter=('created','modified')


    # ver de forma mas detallada user con profile
    # fieldsets = (
    #     ('Profile', {
    #         'fields': (('user', 'picture'),),
    #     }),
    #     ('Extra info', {
    #         'fields': (
    #             ('website', 'phone_number'),
    #             ('biography')
    #         )
    #     }),
    #     ('Metadata', {
    #         'fields': (('created', 'modified'),),
    #     })
    # )

    # readonly_fields = ('created', 'modified',)
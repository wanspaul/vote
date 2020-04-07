from django.contrib import admin

from song.models import ApplySong, VoteLimit

admin.site.register(ApplySong)
admin.site.register(VoteLimit)
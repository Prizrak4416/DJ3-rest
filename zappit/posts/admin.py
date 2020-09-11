from django.contrib import admin
from .models import Post, Vote


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'created')
    list_display_links = ('id', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Vote)

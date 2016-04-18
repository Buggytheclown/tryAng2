from django.contrib import admin
from PiParse.models import PiPosts, PostContents


class PiPostsAdmin (admin.ModelAdmin):
    list_display = ['p_id', 'rating', 'post_link', 'title', 'timestamp']
    list_filter = ['timestamp',]
admin.site.register(PiPosts, PiPostsAdmin)


class PiPostsAdmin (admin.ModelAdmin):
    list_display = ['type', 'pre_content', 'content', 'post']
    list_filter = ['type',]
admin.site.register(PostContents, PiPostsAdmin)
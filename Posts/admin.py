from django.contrib import admin

# Register your models here.
from Posts.models import Posts


class PostsAdmin(admin.ModelAdmin):
    model = Posts

admin.site.register(Posts, PostsAdmin)
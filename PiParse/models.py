from django.contrib.auth.models import User
from django.db import models


class PiPosts(models.Model):
    p_id = models.IntegerField(unique=True)
    rating = models.IntegerField()
    post_link = models.TextField()
    title = models.TextField()
    timestamp = models.DateTimeField()
    description = models.TextField(blank=True, default='')
    viewed = models.ManyToManyField(User, related_name='viewed')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-rating", ]


class PostContents(models.Model):
    type = models.CharField(max_length=10)
    pre_content = models.TextField(blank=True)
    content = models.TextField()
    post = models.ForeignKey(PiPosts, related_name='contents')

    class Meta:
        ordering = ["id", ]

# TODO make InviteList
class FriendList(models.Model):
    user_1 = models.ForeignKey(User, related_name='user_1')
    user_2 = models.ForeignKey(User, related_name='user_2')
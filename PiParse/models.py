from django.contrib.auth.models import User
from django.db import models


class PiPosts(models.Model):
    p_id = models.IntegerField(primary_key=True)
    rating = models.IntegerField()
    post_link = models.TextField()
    title = models.TextField()
    timestamp = models.DateTimeField()
    description = models.TextField(blank=True, default='')
    viewed = models.ManyToManyField(User, related_name='viewed')
    commentsCount = models.IntegerField()

    def __str__(self):
        return self.title

    def isUser_viewed(self, userId):
        """is that user viewed that post?
        :param  userId: id of user
        :type userId: int

        :return: is user viewed post?
        :rtype: bool
        """

        userViewedFilter = self.viewed.filter(id=userId).values('id')
        return userViewedFilter and True or False

    def friend_viewed_name(self, friendIdList):
        """return new list with user from input list who view that post
        :param friendIdList: List<userId>
        :type  friendIdList: list

        :rtype: list
        :returns: List<userName>
        """

        return self.viewed.filter(id__in=friendIdList).values_list('username', flat=True)

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

    @classmethod
    def getFriendList(cls, userId):
        """Return friendlist for request user
        :param userId: user id
        :type userId: int

        :returns: a list of user id
        :rtype: list
        """

        if isinstance(userId, int):
            userFriendsId = cls.objects.all().filter(user_1=userId).values_list('user_2_id', flat=True)
        else:
            userFriendsId = []
        return userFriendsId

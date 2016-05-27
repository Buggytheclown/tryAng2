from django.contrib.auth.models import User
from rest_framework import serializers

from PiParse.models import PiPosts, PostContents


class PostContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContents
        fields = ('type', 'pre_content', 'content')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class PiPostsSerializer(serializers.ModelSerializer):
    contents = PostContentsSerializer(many=True)
    viewed = serializers.SerializerMethodField()
    friendsViewed = serializers.SerializerMethodField()

    def get_viewed(self, obj):
        return False

    def get_friendsViewed(self, obj):
        return []

    class Meta:
        model = PiPosts
        fields = (
        'id', 'viewed', 'friendsViewed',  'p_id', 'rating', 'post_link', 'title', 'timestamp', 'description', 'contents')

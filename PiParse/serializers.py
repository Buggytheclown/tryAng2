from rest_framework import serializers
from PiParse.models import PiPosts, PostContents


class PostContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContents
        fields = ('type', 'pre_content', 'content')


class PiPostsSerializer(serializers.ModelSerializer):
    contents = PostContentsSerializer(many=True)

    class Meta:
        model = PiPosts
        fields = ('p_id', 'rating', 'post_link', 'title', 'timestamp', 'description', 'contents')
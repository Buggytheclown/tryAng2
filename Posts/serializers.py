from rest_framework import serializers
from Posts.models import Posts


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.DateTimeField(format='iso-8601')
    # DATETIME_FORMAT = 'iso-8601'

    class Meta:
        model = Posts
        fields = ('id', 'title', 'content', 'updated', 'timestamp')

from rest_framework import serializers
from Posts.models import Posts


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('id','title', 'content', 'updated', 'timestamp')

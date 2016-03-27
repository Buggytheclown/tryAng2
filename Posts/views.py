from rest_framework import viewsets

from Posts.models import Posts
from Posts.serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
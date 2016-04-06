from rest_framework import viewsets

from Posts.models import Posts
from Posts.serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Posts.objects.all()
        postFrom = self.request.query_params.get('postFrom', None)
        postTo = self.request.query_params.get('postTo', None)
        if postFrom is not None and postTo is not None:
            postFrom = int(postFrom)
            postTo = int(postTo)
            queryset = queryset.order_by('-id')[postFrom:postTo]
        return queryset
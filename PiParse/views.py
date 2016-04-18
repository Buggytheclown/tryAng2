from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from PiParse.models import PiPosts
from PiParse.serializers import PiPostsSerializer


class PiPostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PiPostsSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        Optionally restricts by filtering against a X query parameter in the URL.
        """
        queryset = PiPosts.objects.all()
        postFrom = self.request.query_params.get('postFrom', None)
        postTo = self.request.query_params.get('postTo', None)
        if postFrom is not None and postTo is not None:
            postFrom = int(postFrom)
            postTo = int(postTo)
            queryset = queryset.order_by('id')[postFrom:postTo]
        return queryset
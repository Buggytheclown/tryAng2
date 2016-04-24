from rest_framework import viewsets

from myLogger.models import myLoggerGroup
from myLogger.serializer import myLoggerGroupSerializer


class myLoggerGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Posts.objects.all()
    serializer_class = myLoggerGroupSerializer
    queryset = myLoggerGroup.objects.all()
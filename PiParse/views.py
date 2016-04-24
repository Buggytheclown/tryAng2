import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from PiParse.models import PiPosts
from PiParse.parseScript import ParsePikabu
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
        date = self.request.query_params.get('date', None)
        dateGot = False
        try:
            day, month, year = str(date).split('-')
            dateFrom = datetime.date(int(year), int(month), int(day))
            delta = datetime.date.today() - dateFrom
            if delta.days <= 0:
                raise AttributeError
            if len(day) == 1:
                day = '0' + day
            if len(month) == 1:
                month = '0' + month
            dateTo = dateFrom + datetime.timedelta(days=1)
            dateGot = True
        except:
            dateTo = datetime.datetime.now()
            dateFrom = dateTo - datetime.timedelta(days=1)

        queryset = queryset.filter(timestamp__gte=dateFrom)
        queryset = queryset.filter(timestamp__lte=dateTo)

        if queryset.count() == 0:
            dateParse = ''
            if dateGot:
                dateParse = day + '-' + month + '-' + year
            newParser = ParsePikabu(date=dateParse, tillPage=1)
            newParser.findAndSetStoryes()

        if postFrom and postTo:
            postFrom = int(postFrom)
            postTo = int(postTo)
            queryset = queryset.order_by('-rating')[postFrom:postTo]
        print(date,dateFrom,dateTo)
        return queryset

import datetime
import json

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from PiParse.models import PiPosts
from PiParse.scripts.rawParseScript import ParsePikabu
from PiParse.scripts.rawParseToSQL import postsSQL, loggsSQL
from PiParse.serializers import PiPostsSerializer
from PiParse.scripts.rawViewedToSQL import ViewedToDB


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
        # TODO make sheduler for update
        queryset = PiPosts.objects.all()
        postFrom = self.request.query_params.get('postFrom', None)
        postTo = self.request.query_params.get('postTo', None)
        date = self.request.query_params.get('date', None)
        dateParse = ""
        try:
            day, month, year = str(date).split('-')
            dateFrom = datetime.date(int(year), int(month), int(day))
            delta = datetime.date.today() - dateFrom
            if delta.days <= 0:
                raise AttributeError
            dateTo = dateFrom + datetime.timedelta(days=1)
            dateParse = ("0" + day)[-2:] + '-' + ("0" + month)[-2:] + '-' + year
        except:
            dateTo = datetime.datetime.now()
            dateFrom = dateTo - datetime.timedelta(days=1)

        queryset = queryset.filter(timestamp__range=(dateFrom, dateTo))

        if postFrom and postTo:
            postFrom = int(postFrom)
            postTo = int(postTo)
            queryset = queryset.order_by('-rating')[postFrom:postTo]
            # parse when nothing yet or update parsed post
            if queryset.count() == 0:  # or postTo % 20 == 0 or postFrom == 0
                #     //20 due to pikabu hold only 20 post per page
                nextpage = postTo // 20 + 1
                newParser = ParsePikabu(date=dateParse, page=nextpage)
                loggs, posts = newParser.findAndSetStoryes()
                postsSQL(posts)
                loggsSQL(loggs)
        return queryset


class saveViewed(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request):
        if request.user.id:
            try:
                body_unicode = request.body.decode('utf-8')
                received_json_data = json.loads(body_unicode)
                viewed = received_json_data['viewed']
            except:
                return JsonResponse({'success': False}, status=400)

            ViewedToDB(request.user.id, viewed)
            return Response({'success': True}, status=201)
        else:
            return JsonResponse({'success': False}, status=401)

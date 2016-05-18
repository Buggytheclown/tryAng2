import datetime
import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from PiParse.models import PiPosts, FriendList
from PiParse.scripts.rawParseScript import ParsePikabu
from PiParse.scripts.rawParseToSQL import postsSQL, loggsSQL
from PiParse.serializers import PiPostsSerializer
from PiParse.scripts.rawViewedToSQL import ViewedToDB


class PiPostsViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # serializer_class = PiPostsSerializer
    # permission_classes = (AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def _get_dateParameter(self, date):
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
        timeRange = (dateFrom, dateTo)
        return dateParse, timeRange

    def _queryset_or_parse(self, querysetCount, postTo, dateParse):
        if querysetCount < 20:  # or postTo % 20 == 0 or postFrom == 0
            #     //20 due to pikabu hold only 20 post per page
            nextpage = postTo // 20 + 1
            newParser = ParsePikabu(date=dateParse, page=nextpage)
            loggs, posts = newParser.findAndSetStoryes()
            postsSQL(posts)
            loggsSQL(loggs)

    def _isUser_viewed_post(self, userviewedName, postid):
        # ___add viewed___ to post -  if authenticated and post is viewed

        userViewedFilter = PiPosts.objects.get(id=postid).viewed.filter(username=userviewedName)
        viewed = userViewedFilter and True or False
        return viewed

    def list(self, request):
        # TODO make sheduler for update
        queryset = PiPosts.objects.all()
        postFrom = request.query_params.get('postFrom', None)
        postTo = request.query_params.get('postTo', None)
        date = request.query_params.get('date', None)

        # set datePatse string for parser and date range for filter
        dateParse, timeRange = self._get_dateParameter(date=date)

        # filter query with request.date or date.now
        queryset = queryset.filter(timestamp__range=timeRange)

        # if not post range - make it [0:19]
        postFrom = postFrom or '0'
        postTo = postTo or '19'
        queryset = queryset.order_by('-rating')[int(postFrom):int(postTo)]

        # parse when nothing yet or update parsed post
        self._queryset_or_parse(querysetCount=queryset.count(), postTo=int(postTo), dateParse=dateParse)

        postSerializer = PiPostsSerializer(queryset, many=True)

        # ___add viewed___ to post -  if authenticated and post is viewed
        userviewedName = request.user.username
        # userviewedName = 'admin'
        userviewedQuery = User.objects.get(username=userviewedName)
        userviewedFriendsQueryset = FriendList.objects.get(owner=userviewedQuery).friends.all()
        userviewedFriendsID = [x.username for x in userviewedFriendsQueryset]

        for post in postSerializer.data:
            postid = post.get('id')
            viewed = self._isUser_viewed_post(userviewedName=userviewedName, postid=postid)
            post.update({"viewed": viewed})

            '''
            __OUTPUT friends who viewed post -- 'friendList':[username1, username2]
            get List of friends for our user
            make list of friend that viewed that post
            add list to serializer
            '''
            viewedFriends = [x for x in userviewedFriendsID if self._isUser_viewed_post(userviewedName=x, postid=postid)]
            post.update({"friendsViewed":viewedFriends})

        return Response(postSerializer.data)


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

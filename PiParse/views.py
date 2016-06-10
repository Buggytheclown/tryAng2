import datetime
import json

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from PiParse.models import PiPosts, FriendList
from PiParse.scripts.parsePikabu import ParseComments,  ParsePikabu
from PiParse.scripts.rawToSQL import postsSQL, loggsSQL, ViewedToDB
from PiParse.serializers import PiPostsSerializer


def getBodyDate(request, param):
    try:
        body_unicode = request.body.decode('utf-8')
        received_json_data = json.loads(body_unicode)
        return received_json_data[param]
    except:
        return None


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

    def _parse_pikabu(self, postTo, dateParse):
        #     //20 due to pikabu hold only 20 post per page
        nextpage = postTo // 20 + 1
        newParser = ParsePikabu(date=dateParse, page=nextpage)
        loggs, posts = newParser.findAndSetStoryes()
        postsSQL(posts)
        loggsSQL(loggs)

    def _isUser_viewed_post(self, userId, postid):
        # ___add viewed___ to post -  if authenticated and post is viewed
        userViewedFilter = PiPosts.objects.get(p_id=postid).viewed.filter(id=userId).values('id')
        return userViewedFilter and True or False

    def list(self, request):
        # TODO make sheduler for update post and rating

        # MAIN POST QUERY
        date = request.query_params.get('date', None)
        dateParse, timeRange = self._get_dateParameter(date=date)

        postFrom = request.query_params.get('postFrom', '0')
        postTo = request.query_params.get('postTo', '19')

        queryset = PiPosts.objects.all().filter(timestamp__range=timeRange).order_by('-rating')[
                   int(postFrom):int(postTo)]

        # parse when nothing yet or update parsed post
        if queryset.count() < 5:  # or postTo % 20 == 0 or postFrom == 0
            self._parse_pikabu(postTo=int(postTo), dateParse=dateParse)

        # SUBQUERY FOR VIEWEDS
        userId = request.user.id
        userFriendsId = []

        # for authenticated:
        if userId:
            userFriendsId = FriendList.objects.all().filter(user_1=userId).values_list('user_2_id', flat=True)

        postSerializer = []
        for post in queryset:
            postData = PiPostsSerializer(post).data
            if userId:
                # set post is viewed by user to try or false
                viewed = self._isUser_viewed_post(userId=userId, postid=post.p_id)
                postData.update({"viewed": viewed})

                # provide friendsName for viewed post friend
                viewedFriends = PiPosts.objects.get(p_id=post.p_id).viewed.filter(id__in=userFriendsId).values_list(
                    'username', flat=True)
                postData.update({"friendsViewed": viewedFriends})

            postSerializer.append(postData)

        return Response(postSerializer)


class saveViewed(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request):
        viewed = getBodyDate(request, 'viewed')
        if viewed:
            ViewedToDB(request.user.id, viewed)
            return JsonResponse({'success': True}, status=201)
        else:
            return JsonResponse({}, status=400)


class Comments(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        url = request.query_params.get('page')
        comments = ParseComments().getComments(url)
        return JsonResponse(comments, safe=False)


class Friendlist(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        """get friendlist of request.user"""
        userId = request.user.id
        FriendslistQuery = FriendList.objects.all().filter(user_1=userId)
        friendsName = [x.user_2.username for x in FriendslistQuery]
        return JsonResponse(friendsName, safe=False)


    def put(self, request):
        """add a new friend"""
        userId = request.user.id
        friendName = getBodyDate(request, 'friend')
        if not friendName:
            return JsonResponse({}, status=400)

        try:
            friend = User.objects.get(username=friendName)
            user = User.objects.get(id=userId)
        except ObjectDoesNotExist:
            return JsonResponse({}, status=204)

        if user != friend:
            # in reason of denormalisation bd
            fl1 = FriendList.objects.get_or_create(user_1=user, user_2=friend)
            fl2 = FriendList.objects.get_or_create(user_1=friend, user_2=user)
        else:
            return JsonResponse({}, status=204)

        response = {'success': True, 'created': [fl1[1], fl2[1]]}
        return JsonResponse(response, status=201)


    def patch(self, request):
        """delete friend"""
        userId = request.user.id
        friendName = getBodyDate(request, 'friend')
        if not friendName:
            return JsonResponse({}, status=400)

        try:
            friend = User.objects.get(username=friendName)
            user = User.objects.get(id=userId)
        except ObjectDoesNotExist:
            return JsonResponse({}, status=204)

        # denormalisation bd
        FriendList.objects.get(user_1=user, user_2=friend).delete()
        FriendList.objects.get(user_1=friend, user_2=user).delete()

        response = {'success': True}
        return JsonResponse(response, status=201)
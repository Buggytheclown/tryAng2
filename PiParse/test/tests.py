from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client, RequestFactory
import datetime

from rest_framework.test import APIClient

from PiParse.models import FriendList
from PiParse.scripts.parsePikabu import ParsePikabu, ParseComments
from PiParse.scripts.rawToSQL import loggsSQL, postsSQL, ViewedToDB
from django.db import connection

from PiParse.test.mockPiPostsViewResponse import anon_15_01_2016
from PiParse.test.mockPiPostsViewResponse import auth_15_01_2016
from PiParse.test.mockPikabuCommentsResult import mockPikabuCommentsResult
from PiParse.test.mockPikabuCommentsSoup import MockPikabuCommentsSoup
from PiParse.test.mockPikabuPostsResult import mockPikabuPostsResult, mockLogger
from PiParse.test.mockPikabuPostsSoup import MockPikabuPostsSoup
from PiParse.views import PiPostsViewSet


class MyBaseTest(TestCase):
    def setUp(self):
        self.URL = ''
        raise NotImplemented

    def logMeIn(self):
        self.user = self.create_user('user1')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def create_user(self, name):
        return User.objects.create_user(name, 'test_password')

    def assert_method_toResponse(self, method, statusCode, requestParam=None, responseBody=None, isLoggedin=True):
        requestParam = requestParam or {}
        if isLoggedin:
            method = getattr(self.client, method)
        else:
            method = getattr(Client(), method)
        response = method(self.URL, requestParam, format='json')
        self.assertEquals(response.status_code, statusCode)
        if responseBody:
            self.assertEquals(response.json(), responseBody)


class ParseToSql(TestCase):
    def test_rawSaveLoggs(self):
        """Testing ability to save loggs to DB"""
        loggs = {'title': 'title_123456', 'logs': [
            {'message': 'mes_111', 'type': 'type_111', 'error': 'error_111'},
            {'message': 'mes_222', 'type': 'type_222', 'error': 'error_222'},
            {'message': 'mes_333', 'type': 'type_333', 'error': 'error_333'},
            {'message': 'mes_444', 'type': 'type_444', 'error': 'error_444'},
            {'message': 'mes_555', 'type': 'type_555', 'error': 'error_555'},
        ]}
        result = [('title_123456', 'mes_111', 'type_111', 'error_111'),
                  ('title_123456', 'mes_222', 'type_222', 'error_222'),
                  ('title_123456', 'mes_333', 'type_333', 'error_333'),
                  ('title_123456', 'mes_444', 'type_444', 'error_444'),
                  ('title_123456', 'mes_555', 'type_555', 'error_555')]
        # __save it__
        loggsSQL(loggs)
        cursor = connection.cursor()
        cursor.execute("""SELECT
                  gr.title,
                  lg.message,
                  lg.type,
                  lg.error
                    FROM (SELECT *
                          FROM myLogger_myloggergroup
                          WHERE title = 'title_123456') AS gr
                      JOIN myLogger_mylogger AS lg ON gr.id = lg.group_id""")
        testRes = cursor.fetchall()
        cursor.close()
        self.assertEqual(result, testRes)

    def test_rawSavePosts(self):
        cursor = connection.cursor()
        self.rawSaveNewPosts(cursor)
        self.rawUpdatePostsRating(cursor)
        cursor.close()

    def rawSaveNewPosts(self, cursor):
        """ Testing ability to save Posts to DB"""
        posts = [{'p_id': '11111', 'commentsCount': '1111', 'timestamp': datetime.datetime(2016, 5, 7, 0, 11, 34),
                  'title': 'title_1', 'rating': '1111', 'description': 'description_1', 'post_link': 'post_link_1',
                  'contents': [
                      {'type': 'p', 'pre_content': 'pre_content_1_1', 'content': 'content_1_1'},
                      {'type': 'p', 'pre_content': 'pre_content_1_2', 'content': 'content_1_2'},
                  ],
                  },
                 {'p_id': '22222', 'commentsCount': '2222', 'timestamp': datetime.datetime(2016, 5, 7, 0, 11, 34),
                  'title': 'title_2', 'rating': '2222', 'description': 'description_2', 'post_link': 'post_link_2',
                  'contents': [
                      {'type': 'p', 'pre_content': 'pre_content_2_1', 'content': 'content_2_1'},
                      {'type': 'p', 'pre_content': 'pre_content_2_2', 'content': 'content_2_2'},
                  ],
                  }
                 ]
        result = [(
            11111, 1111, datetime.datetime(2016, 5, 7, 0, 11, 34), 1111, 'title_1', 'description_1', 'post_link_1', 'p',
            'pre_content_1_1', 'content_1_1'), (
            11111, 1111, datetime.datetime(2016, 5, 7, 0, 11, 34), 1111, 'title_1', 'description_1', 'post_link_1', 'p',
            'pre_content_1_2', 'content_1_2'), (
            22222, 2222, datetime.datetime(2016, 5, 7, 0, 11, 34), 2222, 'title_2', 'description_2', 'post_link_2', 'p',
            'pre_content_2_1', 'content_2_1'), (
            22222, 2222, datetime.datetime(2016, 5, 7, 0, 11, 34), 2222, 'title_2', 'description_2', 'post_link_2', 'p',
            'pre_content_2_2', 'content_2_2')]
        # __save it__
        postsSQL(posts)

        cursor.execute("""SELECT
                  gr.p_id,
                  gr.commentsCount,
                  gr.timestamp,
                  gr.rating,
                  gr.title,
                  gr.description,
                  gr.post_link,
                  lg.type,
                  lg.pre_content,
                  lg.content
                    FROM (SELECT *
                          FROM PiParse_piposts
                          WHERE title = 'title_1' OR title = 'title_2') AS gr
                      JOIN PiParse_postcontents AS lg ON gr.p_id = lg.post_id""")
        testRes = cursor.fetchall()

        # self.assertEqual.__self__.maxDiff = None
        self.assertEqual(result, testRes)

    def rawUpdatePostsRating(self, cursor):
        # rating was changed
        posts = [{'p_id': '11111', 'timestamp': datetime.datetime(2016, 5, 7, 0, 11, 34),
                  'title': 'title_1', 'rating': '5555', 'description': 'description_1', 'post_link': 'post_link_1'
                  },
                 {'p_id': '22222', 'timestamp': datetime.datetime(2016, 5, 7, 0, 11, 34),
                  'title': 'title_2', 'rating': '6666', 'description': 'description_2', 'post_link': 'post_link_2',

                  }
                 ]
        result = [
            (11111, datetime.datetime(2016, 5, 7, 0, 11, 34), 5555, 'title_1', 'description_1', 'post_link_1'),
            (22222, datetime.datetime(2016, 5, 7, 0, 11, 34), 6666, 'title_2', 'description_2', 'post_link_2'),
        ]
        postsSQL(posts)
        cursor.execute("""SELECT
                  post.p_id,
                  post.timestamp,
                  post.rating,
                  post.title,
                  post.description,
                  post.post_link
                  FROM PiParse_piposts AS post
                  WHERE title='title_1' OR title='title_2'""")
        testRes = cursor.fetchall()
        self.assertEqual(result, testRes)

    def test_p_idUnique(self):
        """on new bd asshole"""
        # cursor = connection.cursor()
        # cursor.execute("SELECT COUNT(p_id) FROM PiParse_piposts")
        # countP_ID = cursor.fetchone()
        # cursor.execute("SELECT COUNT(DISTINCT p_id) FROM PiParse_piposts")
        # distinctP_ID = cursor.fetchone()
        # cursor.close()
        # self.assertEqual(countP_ID, (0,))

    def test_rawSaveViewed(self):
        # can save data?
        cursor = connection.cursor()
        viewed = [11111, 22222, 33333, 44444, 55555]
        userid = 123
        result = [(11111,), (22222,), (33333,), (44444,), (55555,)]
        ViewedToDB(userid, viewed)
        cursor.execute("SELECT piposts_id FROM PiParse_piposts_viewed WHERE user_id=123")
        testRes = cursor.fetchall()
        self.assertEqual(result, testRes)

        # can save-ignore data?
        viewed2 = [44444, 55555, 66666, 77777, 88888]
        result2 = [(11111,), (22222,), (33333,), (44444,), (55555,), (66666,), (77777,), (88888,), ]
        ViewedToDB(userid, viewed2)
        cursor.execute("SELECT piposts_id FROM PiParse_piposts_viewed WHERE user_id=123")
        testRes2 = cursor.fetchall()
        self.assertEqual(result2, testRes2)
        cursor.close()


class parsePikabu(TestCase):
    def test_parsePikabuPosts(self):
        class MockParsePikabuPosts(ParsePikabu, MockPikabuPostsSoup):
            pass

        pp = MockParsePikabuPosts()
        _, posts = pp.findAndSetStoryes()
        self.assertEqual(posts, mockPikabuPostsResult)

    def test_parsePikabuComments(self):
        class MockParsePikabuComments(ParseComments, MockPikabuCommentsSoup):
            pass

        pc = MockParsePikabuComments()
        comments = pc.getComments('')
        self.assertEqual(comments, mockPikabuCommentsResult)
        # pass


class FriendlistView(MyBaseTest):
    """user playing with friendlist"""

    def setUp(self):
        self.URL = '/api/friendlist/'
        self.logMeIn()

        self.userFriends = ['friend1', 'friend2', 'friend3']
        for friend in self.userFriends:
            userFriend = self.create_user(friend)
            self.make_friend(self.user, userFriend)

    def make_friend(self, user1, user2):
        FriendList.objects.create(user_1=user1, user_2=user2)
        FriendList.objects.get_or_create(user_1=user2, user_2=user1)

    def friendlistDoesNotChanged(self):
        self.assert_method_toResponse('get', 200, responseBody=self.userFriends)

    def test_get(self):
        self.friendlistDoesNotChanged()

    def test_put(self):
        """common put and assert for changes"""
        newFriend = self.create_user('newFriend')
        newUserFriends = self.userFriends[:]
        newUserFriends.append(newFriend.username)

        self.assert_method_toResponse('put', 201, requestParam={'friend': newFriend.username},
                                      responseBody={'success': True, 'created': [True, True]})
        self.assert_method_toResponse('get', 200, responseBody=newUserFriends)

    def test_put_badFriend(self):
        """put with unexisting user"""
        self.assert_method_toResponse('put', 204, requestParam={'friend': 'userDoesNotExist'})
        self.friendlistDoesNotChanged()

    def test_put_badFriend_body(self):
        """put wrong body parameter"""
        self.assert_method_toResponse('put', 400, requestParam={'paramDoesNotExist': self.userFriends[0]})
        self.friendlistDoesNotChanged()

    def test_put_userEQfriend(self):
        """put request.user is friend"""
        self.assert_method_toResponse('put', 204, requestParam={'friend': self.user.username})
        self.friendlistDoesNotChanged()

    def test_patch(self):
        """delete friend"""
        self.assert_method_toResponse('patch', 201, requestParam={'friend': self.userFriends[0]},
                                      responseBody={'success': True})
        self.assert_method_toResponse('get', 200, responseBody=self.userFriends[1:])

    def test_patch_badFriend(self):
        """patch with unexisting user"""
        self.assert_method_toResponse('patch', 204, requestParam={'friend': 'userDoesNotExist'})
        self.friendlistDoesNotChanged()

    def test_patch_badFriend_body(self):
        """patch wrong body parameter"""
        self.assert_method_toResponse('patch', 400, requestParam={'paramDoesNotExist': self.userFriends[0]})
        self.friendlistDoesNotChanged()

    def test_get_put_patch_anonimus(self):
        """unauthenticated goes in ass...401!"""
        client = Client()
        methods = ['put', 'get', 'patch']
        for method in methods:
            self.assert_method_toResponse(method, 401, requestParam={'friend': self.userFriends[0]}, isLoggedin=False)


class saveViewedView(MyBaseTest):
    def setUp(self):
        self.URL = '/api/viewed/'
        self.logMeIn()

    def test_post_goodBody(self):
        self.assert_method_toResponse('post', 201, requestParam={'viewed': [123, 321]}, responseBody={'success': True})

    def test_post_badBody(self):
        self.assert_method_toResponse('post', 400, requestParam={'NotImplemented': [123, 321]})

    def test_post_anonymous(self):
        self.assert_method_toResponse('post', 401, requestParam={'NotImplemented': [123, 321]}, isLoggedin=False)


class CommentsView(MyBaseTest):
    def setUp(self):
        self.URL = '/api/comments/'
        self.logMeIn()

    def test_get(self):
        self.assert_method_toResponse('get', 200, requestParam={'page': ''}, isLoggedin=False)

    def test_get_badParam(self):
        self.assert_method_toResponse('get', 200, requestParam={'NotImplemented': ''}, isLoggedin=False)


class PiPostsView(MyBaseTest):
    fixtures = ['test2']

    def setUp(self):
        self.URL = '/api/PiParse/'
        self.client = APIClient()
        self.user = User.objects.get(id=1)
        self.client.force_authenticate(user=self.user)

    def assert_dateParameters(self, requestDate, rawDate, rawTimeRange):
        responseDate, responseTimeRange = PiPostsViewSet._get_dateParameter(requestDate)
        self.assertEquals(responseDate, rawDate)
        self.assertEquals(responseTimeRange, rawTimeRange)

    def test_dateParameterPast(self):
        days = range(1, 28)
        months = range(1, 12)
        for month in months:
            for day in days:
                requestDate = "{}-{}-2015".format(day, month)
                rawDate = "{}-{}-2015".format(("0" + str(day))[-2:], ("0" + str(month))[-2:])
                rawTimeRange = (datetime.date(2015, month, day), datetime.date(2015, month, day + 1))
                self.assert_dateParameters(requestDate, rawDate, rawTimeRange)

    def test_dateParameterNow(self):
        responseDate, responseTimeRange = PiPostsViewSet._get_dateParameter('')
        self.assertEquals(responseDate, "")

    def test_get_authenticated(self):
        self.assert_method_toResponse('get', 200, requestParam={'date': '15-01-2016'},
                                      responseBody=auth_15_01_2016)

        self.assert_method_toResponse('get', 200, requestParam={'date': '15-01-2016', 'postFrom': '0',
                                                                'postTo': '10'}, responseBody=auth_15_01_2016[0:10])

    def test_get_anonymous(self):
        self.assert_method_toResponse('get', 200, requestParam={'date': '15-01-2016'},
                                      responseBody=anon_15_01_2016, isLoggedin=False)

        self.assert_method_toResponse('get', 200, requestParam={'date': '15-01-2016', 'postFrom': '0', 'postTo': '10'},
                                      responseBody=anon_15_01_2016[0:10], isLoggedin=False)

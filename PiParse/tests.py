from django.test import TestCase
import datetime

# Create your tests here.
from PiParse.scripts.rawParseToSQL import loggsSQL, postsSQL
from django.db import connection
from PiParse.scripts.rawViewedToSQL import ViewedToDB

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
        posts = [{'p_id': '11111', 'timestamp': datetime.datetime(2016, 5, 7, 0, 11, 34),
                  'title': 'title_1', 'rating': '1111', 'description': 'description_1', 'post_link': 'post_link_1',
                  'contents': [
                      {'type': 'p', 'pre_content': 'pre_content_1_1', 'content': 'content_1_1'},
                      {'type': 'p', 'pre_content': 'pre_content_1_2', 'content': 'content_1_2'},
                  ],
                  },
                 {'p_id': '22222', 'timestamp': datetime.datetime(2016, 5, 7, 0, 11, 34),
                  'title': 'title_2', 'rating': '2222', 'description': 'description_2', 'post_link': 'post_link_2',
                  'contents': [
                      {'type': 'p', 'pre_content': 'pre_content_2_1', 'content': 'content_2_1'},
                      {'type': 'p', 'pre_content': 'pre_content_2_2', 'content': 'content_2_2'},
                  ],
                  }
                 ]
        result = [(
            11111, datetime.datetime(2016, 5, 7, 0, 11, 34), 1111, 'title_1', 'description_1', 'post_link_1', 'p',
            'pre_content_1_1', 'content_1_1'), (
            11111, datetime.datetime(2016, 5, 7, 0, 11, 34), 1111, 'title_1', 'description_1', 'post_link_1', 'p',
            'pre_content_1_2', 'content_1_2'), (
            22222, datetime.datetime(2016, 5, 7, 0, 11, 34), 2222, 'title_2', 'description_2', 'post_link_2', 'p',
            'pre_content_2_1', 'content_2_1'), (
            22222, datetime.datetime(2016, 5, 7, 0, 11, 34), 2222, 'title_2', 'description_2', 'post_link_2', 'p',
            'pre_content_2_2', 'content_2_2')]
        # __save it__
        postsSQL(posts)

        cursor.execute("""SELECT
                  gr.p_id,
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
                      JOIN PiParse_postcontents AS lg ON gr.id = lg.post_id""")
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

    # def test_p_idunique(self):
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT COUNT(p_id) FROM PiParse_piposts")
    #     a = cursor.fetchone()
    #     cursor.execute("SELECT COUNT(DISTINCT p_id) FROM PiParse_piposts")
    #     b = cursor.fetchone()
    #     cursor.close()
    #     self.assertEqual(a, b)

    def test_rawSaveViewed(self):
        # can save data?
        cursor = connection.cursor()
        viewed = [11111, 22222, 33333, 44444, 55555]
        userid = 123
        result = [(11111,), (22222,), (33333,), (44444,), (55555,) ]
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
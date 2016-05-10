import datetime

import pytz
from django.db import connection


def postsSQL(posts):
    # Interface posts:<{'p_id': int,
    #                   'post_link': str,
    #                   'title': str,
    #                   'rating': int,
    #                   'timestamp': dateTime,
    #                   'description': str,
    #                   'contents': <{ 'type': str,
    #                                   'pre_content': str,
    #                                   'content': str
    #                                }>
    #                  }>
    cursor = connection.cursor()
    postsids = ""
    for post in posts:
        postid = '{} ,'.format(post['p_id'])
        postsids += postid
        # cursor.execute("SELECT id FROM PiParse_piposts WHERE p_id=%s", [post['p_id']])
        # currentObject = cursor.fetchone()
    sql = "SELECT p_id, id FROM PiParse_piposts WHERE p_id in ({})".format(postsids[:-2])
    cursor.execute(sql)
    # currentObjects like = [(1418,), (1419,), (1421,), (1422,),] or []
    currentObjects = cursor.fetchall()

    # save all or update all
    if len(posts) != len(currentObjects):
        sqlPosts = """INSERT OR REPLACE INTO PiParse_piposts (p_id, rating, post_link, title, timestamp, description) VALUES """
        for post in posts:
            sqlPostsValue = '({}, {}, "{}", "{}", "{}", "{}"), '.format(post['p_id'], post['rating'], post['post_link'], post['title'], post['timestamp'], post['description'])
            sqlPosts += sqlPostsValue
        # return sqlPosts[:-2]
        cursor.execute(sqlPosts[:-2])
        cursor.fetchall()

        sql = "SELECT p_id, id FROM PiParse_piposts WHERE p_id in ({})".format(postsids[:-2])
        cursor.execute(sql)
        # currentObjects like = {4142025: 1, 4142946: 9, 4142899: 16}
        newCurrentObjects = dict(cursor.fetchall())

        sqlContent = """INSERT INTO PiParse_postcontents (type, pre_content, content, post_id) VALUES  """
        for post in posts:
            for content in post['contents']:
                sqlContentValue = '("{}", "{}", "{}", {}), '.format(content['type'], content['pre_content'], content['content'], newCurrentObjects[int(post['p_id'])])
                sqlContent += sqlContentValue
        # return sqlContent
        cursor.execute(sqlContent[:-2])
        cursor.fetchall()
        cursor.close()
    else:
        # ipdate posts rating
        tosqlWhenP_id = ""
        tosqlIn = ""
        for post in posts:
            _p_id = post['p_id']
            tosqlWhenP_id += "WHEN {} THEN {} ".format(_p_id,  post['rating'])
            # return tosqlWhenP_id
            tosqlIn += "{}, ".format(_p_id)

        sqlPosts = "UPDATE PiParse_piposts SET rating = CASE p_id {} END WHERE p_id IN ({})".format(tosqlWhenP_id, tosqlIn[:-2])
        cursor.execute(sqlPosts)
        cursor.fetchall()


def loggsSQL(loggs):
    # {'title': str,
    #  'logs': <{'type': str,
    #            'message': str
    #            'error': str}>
    # }
    cursor = connection.cursor()
    now = str(datetime.datetime.now())
    cursor.execute("INSERT INTO myLogger_myloggergroup (title, timestamp) VALUES (%s, %s)", [loggs['title'], now])
    cursor.fetchall()
    cursor.execute("SELECT id FROM myLogger_myloggergroup ORDER BY timestamp DESC LIMIT 1")
    groupID = cursor.fetchone()[0]
    stuckLoggs = """INSERT INTO myLogger_mylogger (type, message, error, group_id, timestamp) VALUES """
    for log in loggs['logs']:
        now = str(datetime.datetime.now())
        stuckLog = '("{}", "{}", "{}", {}, "{}"), '.format(log['type'], log['message'], log['error'], groupID, now)
        stuckLoggs += stuckLog
        # cursor.execute("INSERT INTO myLogger_mylogger (type, message, error, group_id, timestamp) VALUES (%s, %s, %s, %s, %s)", [log['type'], log['message'], log['error'], groupID, now])
    cursor.execute(stuckLoggs[:-2])
    cursor.fetchall()
    cursor.close()
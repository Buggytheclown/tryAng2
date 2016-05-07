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
    for post in posts:
        cursor.execute("SELECT id FROM PiParse_piposts WHERE p_id=%s", [post['p_id']])
        currentObject = cursor.fetchone()
        if not currentObject:
            cursor.execute(
                "INSERT INTO PiParse_piposts (p_id, rating, post_link, title, timestamp, description) VALUES (%s, %s, %s, %s, %s, %s)",
                [post['p_id'], post['rating'], post['post_link'], post['title'], post['timestamp'],
                 post['description']])
            cursor.fetchone()
            cursor.execute("SELECT id FROM PiParse_piposts WHERE p_id = %s", [post['p_id']])
            currentObjectID = cursor.fetchone()[0]
            for content in post['contents']:
                cursor.execute(
                    "INSERT INTO PiParse_postcontents (type, pre_content, content, post_id) VALUES (%s, %s, %s, %s)",
                    [content['type'], content['pre_content'], content['content'], currentObjectID])
                cursor.fetchone()

        else:
            cursor.execute("UPDATE PiParse_piposts SET rating = %s WHERE p_id = %s", [post['rating'], post['p_id']])
    cursor.close()


def loggsSQL(loggs):
    # {'title': str,
    #  'logs': <{'type': str,
    #            'message': str
    #            'error': str}>
    # }
    cursor = connection.cursor()
    now = str(datetime.datetime.now(pytz.UTC))
    cursor.execute("INSERT INTO myLogger_myloggergroup (title, timestamp) VALUES (%s, %s)", [loggs['title'], now])
    cursor.fetchone()
    cursor.execute("SELECT id FROM myLogger_myloggergroup ORDER BY timestamp DESC LIMIT 1")
    groupID = cursor.fetchone()[0]
    stuckLoggs = """INSERT INTO myLogger_mylogger (type, message, error, group_id, timestamp) VALUES """
    for log in loggs['logs']:
        now = str(datetime.datetime.now(pytz.UTC))
        stuckLog = '("{}", "{}", "{}", {}, "{}"), '.format(log['type'], log['message'], log['error'], groupID, now)
        stuckLoggs += stuckLog
                    # cursor.execute("INSERT INTO myLogger_mylogger (type, message, error, group_id, timestamp) VALUES (%s, %s, %s, %s, %s)", [log['type'], log['message'], log['error'], groupID, now])
    cursor.execute(stuckLoggs[:-2])
    cursor.fetchall()
    cursor.close()

# from PiParse.test.rawCursorFetchall import fetch
from django.db import connection

def fetch(*sql):
    cursor = connection.cursor()
    cursor.execute(*sql)
    return cursor.fetchall()

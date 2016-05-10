# from PiParse.test.testParseToSQL import timetestit
# from PiParse.test.testParseToSQL import testit

from timeit import Timer

from PiParse.scripts.rawParseScript import ParsePikabu
from PiParse.scripts.rawParseToSQL import postsSQL, loggsSQL
# import os
# import sys
#
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'tryAng.settings'
# sys.path.append('../../')


def timetestit(date=''):
    t = Timer(lambda: testit(date))
    return t.timeit(number=1)


def testit(date=''):
    posts = ParsePikabu(date=date)
    # posts.getParsePage("http://pikabu.ru/best")
    # an = posts.getParsePage("http://pikabu.ru/best")
    loggs, posts = posts.findAndSetStoryes()
    # postsSQL(posts)
    # loggsSQL(loggs)
    return posts

# if __name__=="__main__":
#     timetestit()
# from PiParse.scripts.parseComments import ParseComments
from functools import reduce

from bs4 import BeautifulSoup
import re
from pip._vendor.requests.packages import urllib3


class ParseComments:
    def getParsePage(self, parseUrl):
        http = urllib3.PoolManager()
        http.headers['user_name'] = 'Tidjei'
        http.headers['password'] = 'buggy2497672'
        response = http.request('GET', parseUrl)
        return BeautifulSoup(response.data, "html5lib")

    def getRawComments(self, soup):
        mainCommentsBlock = soup.find("div", class_='b-comments_type_main')
        comments = mainCommentsBlock.find_all("div", class_="b-comment", recursive=False)
        return comments

    def getRawCommentBody(self, rawcomment):
        return rawcomment.find("div", class_='b-comment__body')

    def parseHeader(self, rawCommentBody):
        rawHeader = rawCommentBody.find("div", class_='b-comment__header')
        rating = rawHeader.find(class_='b-comment__rating-count')
        ratingBlocked = rating.find(class_="i-sprite--comments__rating-lock")
        if ratingBlocked:
            rating = 'blocked'
        else:
            rating = rating.contents[0]

        commentUser = rawHeader.find(class_='b-comment__user')
        useravatar = None
        username = commentUser.find("a").find('span').contents[0]
        time = commentUser.find("time")['datetime']

        return useravatar, username, rating, time

    def parseContent(self, rawCommentBody):
        # TODO test it
        rawcomment = rawCommentBody.find("div", class_='b-comment__content').contents
        # concat Array<string> in type:string
        rawcomment = map(lambda x: str(x).replace('"', "\'"), rawcomment)
        rawcomment = reduce(lambda x, y: x + y, rawcomment)
        return rawcomment

    def findChilds(self, rawcomment):
        childsBlock = rawcomment.find("div", class_='b-comments_level_0')
        if childsBlock:
            childs = childsBlock.find_all("div", class_='b-comment', recursive=False)
        else:
            childs = []
        return childs

    def findComments(self, rawcomments):
        output = []
        for rawcomment in rawcomments:
            rawCommentBody = self.getRawCommentBody(rawcomment)
            useravatar, username, rating, time = self.parseHeader(rawCommentBody)
            content = self.parseContent(rawCommentBody)
            child = self.findChilds(rawcomment)
            if child:
                child = self.findComments(child)
            # 'content':content,
            comment = {'username': username, 'useravatar': useravatar, 'rating': rating, 'time': time, 'content':content, 'child': child}
            output.append(comment)
        return output

    def getComments(self, pageurl):
        soup = self.getParsePage(parseUrl=pageurl)
        rawcomments = self.getRawComments(soup)
        comments = self.findComments(rawcomments)
        return comments

from functools import reduce

import datetime

import pytz
from bs4 import BeautifulSoup
import re

from pip._vendor.requests.packages import urllib3

from myLogger.rawLoggertry import logger_try_or_none, logger_write


class ParsePikabu:
    def __init__(self, date='', tillPage=None, tillRating=None, page=None):
        if date:
            date = '/' + str(date)
        self.date = date
        self.tillPage = tillPage
        self.tillRating = tillRating
        self.currentPage = page or 1
        self.lastRating = None
        self.page = page
        # protected name newLogger is used in loggertry
        self._newLogger = {'title': 'trying date={}, tillPage={}, tillRating={}, page={}'.format(date, tillPage, tillRating, page),
                           'logs': []}
        self._newPosts = []

    @logger_try_or_none(type='error', message='getParsePage try to get a soup HTML')
    def getParsePage(self, parseUrl):
        http = urllib3.PoolManager()
        http.headers['user_name'] = 'Tidjei'
        http.headers['password'] = 'buggy2497672'
        response = http.request('GET', parseUrl)
        return BeautifulSoup(response.data, "html5lib")

    def createPost(self, p_id, link, theme, rating, timestamp, description):

        newPost = {'p_id': p_id, 'post_link': link, 'title': theme, 'rating': rating, 'timestamp': timestamp,
                   'description': description, 'contents': []}
        logger_write(group=self._newLogger, type='info', message='Post was created: {}'.format(theme))
        return newPost

    @logger_try_or_none(type='error', message='setPost fail to set a post date')
    def setPost(self, table):
        # link = ''
        # theme = ''
        # timestamp = ''
        story_description = ''
        p_id = table['data-story-id']
        story_link = table.find("a", class_='story__title-link')
        link = story_link['href']
        theme = story_link.contents[0].replace('"', "\'")
        _story_description = table.find("div", class_='story__description')
        if _story_description and _story_description.contents:
            story_description = str(_story_description.contents[0])
        story_rating = table.find("div", class_='story__rating-count').contents[0].replace('\n', '').replace('\t', '')
        timestamp = table.find("div", class_='story__date')['title']
        # small no UTC fix (
        timestamp = datetime.datetime.utcfromtimestamp(int(timestamp)) + datetime.timedelta(
            hours=3) + datetime.timedelta(minutes=30)
        # timestamp = pytz.utc.localize(timestamp)

        if len(p_id) > 3:
            # story_rating = story_rating.contents[0]
            self.lastRating = story_rating
            newPost = self.createPost(p_id=p_id, link=link, theme=theme, rating=story_rating, timestamp=timestamp,
                                      description=story_description)
            return newPost
        else:
            return None

    @logger_try_or_none(type='error', message='createContent fail to save a post content')
    def createContent(self, newPost, type, content, pre_content):
        if newPost and type and content:
            newPost['contents'].append({'type': type, 'pre_content': pre_content, 'content': content})
        else:
            raise AttributeError('wrong content on post:', newPost)

    @logger_try_or_none(type='error', message='setContent fail to set a post content')
    def setContent(self, newPost, content):
        post_content_type = ''
        post_content = ''
        post_pre_content = ''

        content_class = content['class'][1]
        if re.match("b-story(-block|__content)_type_text", content_class):
            post_content = content.contents
            if content.find(class_='b-story-block__content'):
                post_content = content.find(class_='b-story-block__content').contents
            # concat Array<string> in type:string
            post_content = map(lambda x: str(x).replace('"', "\'"), post_content)
            post_content = reduce(lambda x, y: x + y, post_content)
            post_content_type = 'p'

        elif re.match("b-story(-block|__content)_type_(media|image|video)", content_class):
            if content.find(class_='b-gifx'):
                post_content = content.find('a')['href']
                post_pre_content = content.find('img')['src']
                post_content_type = 'gif'

            elif content.find(class_='b-video'):
                post_content = content.find(class_='b-video')['data-url']
                # style="background-image: url(http://s8.pikabu.ru/video/2016/04/13/9/1460552931830.jpg); " or url('')
                pre_video = content.find(class_='b-video__preview')['style']
                http_start = pre_video.find('http')
                http_end = pre_video.find('.jpg')
                post_pre_content = pre_video[http_start:http_end + 4]
                post_content_type = 'video'

            else:
                try:
                    post_content = content.find('img')['data-src']
                except:
                    post_content = content.find('img')['src']
                post_content_type = 'img'

        else:
            return False

        if post_content_type and post_content:
            self.createContent(newPost=newPost, type=post_content_type,
                               content=post_content, pre_content=post_pre_content)
            return True
        else:
            return False

    @logger_try_or_none(type='error', message='findTables fail')
    def findTables(self, soup):
        return soup.findAll("div", class_='story')

    @logger_try_or_none(type='error', message='findContents fail')
    def findContents(self, table):
        contents = table.find(class_='story__wrapper')
        contents = contents.findAll(class_=re.compile("b-story(-block|__content)_type_\w+"))
        return contents

    def setNewPage(self):
        if not self.page and self.tillPage and self.tillPage > self.currentPage or not self.page and self.tillRating and self.tillRating <= self.lastRating:
            self.currentPage += 1
            return True
        else:
            return False

    def findAndSetStoryes(self):
        parseUrl = "http://pikabu.ru/best" + self.date + "?page=" + str(self.currentPage)
        soup = self.getParsePage(parseUrl=parseUrl)
        if not soup:
            return False
        tables = self.findTables(soup)
        if not tables:
            return False
        for table in tables:
            newPost = self.setPost(table=table)
            if not newPost:
                continue

            # find All div with (text, image, media, video)
            contents = self.findContents(table)
            if not contents:
                logger_write(group=self._newLogger, type='warning',
                             message='Post was deleted: {}'.format(newPost['title']))
                # newPost.delete() - in our case just not append it
                continue

            # decide what type of content we have and do smth
            for content in contents:
                if not self.setContent(newPost=newPost, content=content):
                    logger_write(group=self._newLogger, type='warning',
                                 message='Post was deleted: {}'.format(newPost['title']))
                    # newPost.delete()
                    break
            # if not break )
            else:
                self._newPosts.append(newPost)
        while self.setNewPage():
            self.findAndSetStoryes()
        return self._newLogger, self._newPosts

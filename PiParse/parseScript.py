from functools import reduce

import datetime
from bs4 import BeautifulSoup
import re
from pip._vendor.requests.packages import urllib3
from PiParse.models import PiPosts, PostContents


class ParsePikabu:
    def __init__(self, bestPage=None, urlPage=None):
        if bestPage and not urlPage:
            self._url = "http://pikabu.ru/best?page=" + bestPage
        elif urlPage and not bestPage:
            self._url = urlPage
        else:
            raise AttributeError('init can have only bestPage or urlPage ')

    def getParsePage(self):
        http = urllib3.PoolManager()
        http.headers['user_name'] = 'Tidjei'
        http.headers['password'] = 'buggy2497672'
        response = http.request('GET', self._url)
        return BeautifulSoup(response.data, "html.parser")

    def createPost(self, p_id, link, theme, rating, timestamp):
        newPost = PiPosts(p_id=p_id, post_link=link, title=theme, rating=rating, timestamp=timestamp)
        newPost.save()
        return newPost

    def setPost(self, table):
        link = ''
        theme = ''
        timestamp = ''
        p_id = table['data-story-id']
        story_link = table.find(class_='story__title-link')
        if story_link:
            link = story_link['href']
            theme = story_link.contents[0]
        story_rating = table.find(class_='story__rating-count')
        timestamp = table.find(class_='story__date')['title']
        timestamp = datetime.datetime.utcfromtimestamp(int(timestamp))
        if len(p_id) > 3 and link and theme and story_rating and timestamp:
            story_rating = story_rating.contents[0]
            newPost = self.createPost(p_id=p_id, link=link, theme=theme, rating=story_rating, timestamp=timestamp)
            return newPost
        else:
            return None

    def createContent(self, newPost, type, content, pre_content):
        if newPost and type and content:
            newContent = PostContents(post=newPost, type=type, pre_content=pre_content, content=content)
            newContent.save()
        else:
            raise AttributeError('wrong content on post:', newPost)

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
            post_content = map(lambda x: str(x), post_content)
            post_content = reduce(lambda x, y: x + y, post_content)
            post_content_type = 'p'

        elif re.match("b-story(-block|__content)_type_(media|image|video)", content_class):
            if content.find(class_='b-gifx'):
                post_content = content.find('a')['href']
                post_pre_content = content.find('img')['src']
                post_content_type = 'gif'

            elif content.find(class_='b-video'):
                post_content = content.find(class_='b-video')['data-url']
                # style="background-image: url(http://s8.pikabu.ru/video/2016/04/13/9/1460557993222931830.jpg); "
                pre_video = content.find(class_='b-video__preview')['style']
                http_start = pre_video.find('http')
                http_end = pre_video.find(');')
                post_pre_content = pre_video[http_start:http_end]
                post_content_type = 'video'

            else:
                try:
                    post_content = content.find('img')['data-src']
                except:
                    post_content = content.find('img')['src']
                post_content_type = 'img'

        else:
            print('!!!!!!!!!Smth goes wrong!!!!!')

        if post_content_type and post_content:
            self.createContent(newPost=newPost, type=post_content_type,
                               content=post_content, pre_content=post_pre_content)
        else:
            return None

    def findAndSetStoryes(self):
        soup = self.getParsePage()
        if not soup:
            return None
        tables = soup.findAll("div", class_='story')
        if not tables:
            return None
        for table in tables:
            newPost = self.setPost(table=table)
            if not newPost:
                continue

            # find All div with (text, image, media, video)
            contents = table.find(class_='story__wrapper')
            contents = contents.findAll(class_=re.compile("b-story(-block|__content)_type_\w+"))
            if not contents:
                return None

            # decide what type of content we have and do smth
            for content in contents:
                self.setContent(newPost=newPost, content=content)
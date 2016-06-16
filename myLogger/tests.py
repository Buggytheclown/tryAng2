from django.test import TestCase

# Create your tests here.
from myLogger.rawLoggertry import logger_write, logger_try_or_none


class logerTest(TestCase):
    def test_loger(self):

        class TestTheLogger:
            def __init__(self):
                self._newLogger = {'title': 'test the logger', 'logs': []}

            def loggerWrite(self):
                logger_write(group=self._newLogger, type='msg', message='1st message')

            @logger_try_or_none(type='err', message='catch the err')
            def someErr(self):
                raise AttributeError('Raised err')

            @logger_try_or_none(type='noterr', message='!catch the err')
            def someErrUncaught1(self):
                story_rating = None
                rating = story_rating['href']

            @logger_try_or_none(type='noterr2', message='!catch the err')
            def someErrUncaught2(self):
                story_link = None
                rating = story_link['href']

            def doWork(self):
                self.loggerWrite()
                self.someErr()
                self.someErrUncaught1()
                self.someErrUncaught2()

            @property
            def loggs(self):
                return self._newLogger

        testLogger = TestTheLogger()
        testLogger.doWork()
        loggs = testLogger.loggs

        mockLoggs = {'title': 'test the logger', 'logs': []}
        mockLogMsg = {'type': 'msg', 'message': '1st message', 'error': ''}
        mockLogErr = {'type': 'err', 'message': 'catch the err', 'error': 'AttributeError: Raised err'}

        mockLoggs['logs'].append(mockLogMsg)
        mockLoggs['logs'].append(mockLogErr)

        self.maxDiff = None
        self.assertEquals(loggs['title'], mockLoggs['title'])
        self.assertEquals(len(loggs['logs']), 2)
        self.assertEquals(loggs['logs'][0]['message'], '1st message')
        self.assertEquals(loggs['logs'][1]['message'], 'catch the err')
#!/usr/bin/env/python
# _*_ coding:utf-8_*_

import tweepy

from config import TWITTER_ACCESS_SECRET
from config import TWITTER_ACCESS_TOKEN
from config import TWITTER_CONSUMER_KEY
from config import TWITTER_CONSUMER_SECRET
from handlers.ExceptionHandler import ExceptionHandler


class TweepyHandler(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def tweet_message(self, message):
        """
        Tweets a message.
        :param message:
        :return:
        """
        try:
            self.api.update_status(message)
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

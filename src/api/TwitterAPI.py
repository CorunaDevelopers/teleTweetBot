#!/usr/bin/env/python
# _*_ coding:utf-8_*_

import tweepy


class TwitterAPI(object):

    def __init__(self, consummer_key, consummer_secret, access_key, access_secret):
        self.consummer_key = consummer_key
        self.consummer_secret = consummer_secret
        self.access_key = access_key
        self.access_secret = access_secret
        auth = tweepy.OAuthHandler(self.consummer_key, self.consummer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(auth)

    def tweet_message(self, message):
        self.api.update_status(message)

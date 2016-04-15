#!/usr/bin/env python
# _*_ coding:utf-8 _*


class TwitterCommand:
    def __init__(self, api):
        self.api = api

    def proccess_message(self, message):
        text = message['text']
        print text

        if text.startswith('/tweet '):
            print 'tweet'
            self.api.tweet_message(text.replace('/tweet ', ''))

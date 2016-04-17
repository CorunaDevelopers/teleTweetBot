#!/usr/bin/env python
# _*_ coding:utf-8 _*

from handlers.ExceptionHandler import ExceptionHandler


class TwitterCommand:
    def __init__(self, api):
        self.api = api

    def process_message(self, telegram_response):
        try:
            text = telegram_response.message.text

            if text.startswith('/tweet '):
                print 'tweet'
                self.api.tweet_message(text.replace('/tweet ', ''))
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

#!/usr/bin/env python
# _*_ coding:utf-8 _*

from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler


# TODO
class MentionsCommand:
    def __init__(self, twitter_api, bot):
        self.twitterApi = twitter_api
        self.bot = bot

    def process_message(self, message):
        try:
            pass
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

#!/usr/bin/env python
# _*_ coding:utf-8 _*

from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler


def process_message(twitter_api, telegram_message):
    try:
        text = telegram_message.message.text
        twitter_api.tweet_message(text.replace('/tweet', ''))
        return '¡Tuiteado! :)'
    except Exception as ex:
        ExceptionHandler.handle_exception(ex, False)

#!/usr/bin/env python
# _*_ coding:utf-8 _*

from teleTweetBot.bot import TeleTweetBot
from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler


def process_message(telegram_message):
    try:
        text = telegram_message.message.text
        TeleTweetBot.twitterAPI.tweet_message(text)
        return '¡Tuiteado! :)'
    except Exception as ex:
        ExceptionHandler.handle_exception(ex, False)

#!/usr/bin/env/python
# _*_ coding:utf-8_*_

from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler


def process_message(telegram_message):
    try:
        # TODO: Remove the user from somewhere
        # user_id = telegram_message.message.message_from.id
        user_first_name = telegram_message.message.message_from.first_name
        return '¡Deica logo, {0}!'.format(user_first_name)
    except Exception as ex:
        ExceptionHandler.handle_exception(ex, False)

#!/usr/bin/env python
# _*_ coding:utf-8 _*

from commands import StartCommand
from commands import StopCommand
from commands import TwitterCommand

from handlers.ExceptionHandler import ExceptionHandler

COMMANDS = {
    '/start': StartCommand.process_message,
    '/stop': StopCommand.process_message,
    '/tweet': TwitterCommand.process_message
}


def process_message(twitter_api, telegram_message):
    try:
        msg_command = telegram_message.message.text.split()[0].lower()
        return COMMANDS[msg_command](twitter_api, telegram_message)
    except Exception as e:
        ExceptionHandler.handle_exception(e, False)

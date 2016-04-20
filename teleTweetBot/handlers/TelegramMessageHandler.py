#!/usr/bin/env python
# _*_ coding:utf-8 _*

import teleTweetBot.commands.StartCommand
import teleTweetBot.commands.StopCommand
import teleTweetBot.commands.TwitterCommand
from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler

COMMANDS = {
    '/start': teleTweetBot.commands.StartCommand.process_message,
    '/stop': teleTweetBot.commands.StopCommand.process_message,
    '/tweet': teleTweetBot.commands.TwitterCommand.process_message
}


def process_message(telegram_message):
    try:
        msg_command = telegram_message.message.text.split()[0].lower()
        return COMMANDS[msg_command](telegram_message)
    except Exception as e:
        ExceptionHandler.handle_exception(e, False)

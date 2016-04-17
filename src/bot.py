#!/usr/bin/env/python
# _*_ coding:utf-8_*_

# consumer key KZInF8Tzh4FuiffKBb3Qt5k4M
# consumer secrete TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx

import time

import telepot

from commands.StartCommand import StartCommand
from commands.StopCommand import StopCommand
from commands.TwitterCommand import TwitterCommand
from config import BOT_TOKEN
from handlers.ExceptionHandler import ExceptionHandler
from handlers.TweepyHandler import TweepyHandler
from src.domain.TelegramResponse import TelegramResponse


class TeleTweetBot:
    def __init__(self):
        self.users = []

        # Twitter
        self.twitterAPI = TweepyHandler()

        # Telegram
        self.bot = self.__get_telepot_instance()
        self.bot.notifyOnMessage(self.__handle_message)

        self.commands = [
            TwitterCommand(self.twitterAPI),
            StartCommand(self.users),
            StopCommand(self.users),
        ]

    @staticmethod
    def __get_telepot_instance():
        """
        Gets an instance of Telepot bot.
        :return:
        """
        try:
            return telepot.Bot(BOT_TOKEN)
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, True)

    def __handle_message(self, message):
        """
        Handles a message sent from telegram.
        :param message:
        :return:
        """
        try:
            content_type, chat_type, chat_id = telepot.glance(message)
            msg = TelegramResponse(content_type, chat_type, chat_id, message)

            # TODO: Do an enum for the content types
            if content_type == 'text':
                print msg.message.text
                user_id = msg.message.message_from.id

            #TODO: Change the command pattern for a strategy
            for command in self.commands:
                response = command.process_message(msg)
                if response:
                    self.bot.sendMessage(user_id, response)
                    break

        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)


if __name__ == '__main__':
    TeleTweetBot()
    while 1:
        time.sleep(10)

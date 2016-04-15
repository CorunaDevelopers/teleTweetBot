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


class TeleTweetBot:
    def __init__(self):
        self.users = []

        self.twitterAPI = self.__get_tweepy_instance()

        self.commands = [
            TwitterCommand(self.twitterAPI),
            StartCommand(self.users),
            StopCommand(self.users),
        ]

        self.bot = self.__get_telepot_instance()
        self.bot.notifyOnMessage(self.__handle_message)

    @staticmethod
    def __get_tweepy_instance():
        """
        Gets an instance of Tweepy API.
        :return:
        """
        try:
            return TweepyHandler()
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, True)

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

            if content_type == 'text':
                print(message['text'])
                user_id = message['from']['id']

                for command in self.commands:
                    response = command.process_message(message)
                    if response:
                        self.bot.sendMessage(user_id, response)
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)


if __name__ == '__main__':
    TeleTweetBot()
    while 1:
        time.sleep(10)

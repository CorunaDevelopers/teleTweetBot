#!/usr/bin/env/python
# _*_ coding:utf-8_*_

# consumer key KZInF8Tzh4FuiffKBb3Qt5k4M
# consumer secrete TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx

import time

import telepot

from config import BOT_TOKEN
from handlers.ExceptionHandler import ExceptionHandler
from handlers.TweepyHandler import TweepyHandler
from domain.TelegramResponse import TelegramResponse
from handlers.TelegramMessageHandler import process_message


class TeleTweetBot:
    def __init__(self):
        self.users = []

        # Twitter
        self.twitter_api = TweepyHandler()
        self.twitter_api.open_stream("@telepaxaro_bot")

        # Telegram
        self.bot = self.__get_telepot_instance()
        self.bot.notifyOnMessage(self.__handle_message)

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
            telegram_message = TelegramResponse(content_type, chat_type, chat_id, message)

            # TODO: Do an enum for the content types
            if content_type == 'text':
                print telegram_message.message.text
                user_id = telegram_message.message.message_from.id

                response = process_message(self.twitter_api, telegram_message)
                if response:
                    self.bot.sendMessage(user_id, response)

        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)


if __name__ == '__main__':
    TeleTweetBot()
    while 1:
        time.sleep(10)

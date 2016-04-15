#!/usr/bin/env/python
# _*_ coding:utf-8_*_

# consumer key KZInF8Tzh4FuiffKBb3Qt5k4M
# consumer secrete TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx

import time

import telepot

from commands.TweetCommand import TweetCommand
from config import *


class TeleTweetBot:

    def __init__(self):
        self.commands = [
            TweetCommand(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)]
        bot = telepot.Bot(BOT_TOKEN)
        bot.notifyOnMessage(self.handle_message)

    def handle_message(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text':
            print(message['text'])
            for command in self.commands:
                command.proccessMessage(message)


def main():
    TeleTweetBot()
    while 1:
        time.sleep(10)


if __name__ == '__main__':
    main()

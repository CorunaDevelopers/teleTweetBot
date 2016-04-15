# consumer key KZInF8Tzh4FuiffKBb3Qt5k4M
# consumer secrete TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx

from config import *
import telepot
from pprint import pprint
import time
from commands.TweetCommand import TweetCommand

class TeleTweetBot:

    def __init__(self):
        self.commands = [ TweetCommand(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET) ]
        bot = telepot.Bot(BOT_TOKEN)
        bot.notifyOnMessage(self.handle_message)

    def handle_message(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text':
            print(message['text'])
            for command in self.commands:
                command.proccessMessage(message)


def main():
    tele_tweet_bot = TeleTweetBot()
    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()



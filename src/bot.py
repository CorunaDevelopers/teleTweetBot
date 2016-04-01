# consumer key KZInF8Tzh4FuiffKBb3Qt5k4M
# consumer secrete TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx

from config import *
import telepot
from pprint import pprint
import time
import tweepy

bot = telepot.Bot(BOT_TOKEN)

def handle_message(message):
    content_type, chat_type, chat_id = telepot.glance(message)

    if content_type == 'text':

        print(message['text'])
        tweet_message(message['text'])

bot.notifyOnMessage(handle_message)

def tweet_message(text):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

    api = tweepy.API(auth)

    api.update_status(text)

while 1:
    time.sleep(10)

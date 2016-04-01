# consumer key KZInF8Tzh4FuiffKBb3Qt5k4M
# consumer secrete TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx


import telepot
from pprint import pprint
import time
import tweepy

bot = telepot.Bot('209263414:AAEesdwt-XtW_XfQhIPp0MHeuG4xZSOafoo')

def handle_message(message):
    content_type, chat_type, chat_id = telepot.glance(message)

    if content_type == 'text':

        print(message['text'])
        tweet_message(message['text'])

bot.notifyOnMessage(handle_message)

def tweet_message(text):
    consumer_key = 'KZInF8Tzh4FuiffKBb3Qt5k4M'
    consumer_secret = 'TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx'
    access_token = '715949543767060480-J3givPfWWxDueUSsOVBC5cklkkkfdsr'
    access_secret = 'Ftm6AjGGw8XOGG5coemPmoMWlzbOKWZDgdhzFxeSqLLbz'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    api.update_status(text)

while 1:
    time.sleep(10)

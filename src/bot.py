# consumer key KZInF8Tzh4FuiffKBb3Qt5k4M
# consumer secrete TEekW9OkM5YmPpBdj1gIZOvBX4Esfu1YM6cZlkSq22iDC98Rmx


import telepot
from pprint import pprint
import time

bot = telepot.Bot('209263414:AAEesdwt-XtW_XfQhIPp0MHeuG4xZSOafoo')

def handle_message(message):
    content_type, chat_type, chat_id = telepot.glance(message)

    if content_type == 'text':
        print(message['text'])

bot.notifyOnMessage(handle_message)

while 1:
    time.sleep(10)
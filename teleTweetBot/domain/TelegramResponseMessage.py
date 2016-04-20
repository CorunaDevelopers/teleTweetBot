#!/usr/bin/env python
# _*_ coding:utf-8 _*

from TelegramResponseChat import TelegramResponseChat
from TelegramResponseEntities import TelegramResponseEntities
from TelegramResponseFrom import TelegramResponseFrom
from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler


class TelegramResponseMessage:
    def __init__(self, response_message):
        try:
            self.chat = TelegramResponseChat(response_message.get('chat'))
            self.date = response_message.get('date')
            self.entities = TelegramResponseEntities(response_message.get('entities'))
            self.message_from = TelegramResponseFrom(response_message.get('from'))
            self.id = response_message.get('message_id')
            self.text = response_message.get('text').encode('utf-8')

            # print '\tResponseMessage'
            # print '\tchat: ' + str(self.chat)
            # print '\tdate: ' + str(self.date)
            # print '\tid: ' + str(self.id)
            # print '\ttext: ' + self.text
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

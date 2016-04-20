#!/usr/bin/env python
# _*_ coding:utf-8 _*

from TelegramResponseMessage import TelegramResponseMessage
from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler


class TelegramResponse():
    def __init__(self, content_type, chat_type, chat_id, message):
        try:
            self.chat_id = chat_id
            self.chat_type = chat_type.encode('utf-8')
            self.content_type = content_type
            self.message = TelegramResponseMessage(message)

            # print 'TelegramResponse:'
            # print 'chat_id: ' + str(self.chat_id)
            # print 'chat_type: ' + self.chat_type
            # print 'content_type: ' + str(self.content_type)
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

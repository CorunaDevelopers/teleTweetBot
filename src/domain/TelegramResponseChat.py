#!/usr/bin/env python
# _*_ coding:utf-8 _*

from ..handlers.ExceptionHandler import ExceptionHandler


class TelegramResponseChat:
    def __init__(self, response_chat):
        try:
            self.first_name = response_chat.get('first_name').encode('utf-8')
            self.id = response_chat.get('id')
            self.type = response_chat.get('type').encode('utf-8')
            self.username = response_chat.get('username').encode('utf-8')

            # print '\tTelegramResponseChat'
            # print '\tfirst_name: ' + self.first_name
            # print '\tid: ' + str(self.id)
            # print '\ttype: ' + self.type
            # print '\tusername: ' + self.username
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

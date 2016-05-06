#!/usr/bin/env python
# _*_ coding:utf-8 _*

from handlers.ExceptionHandler import ExceptionHandler


class TelegramResponseFrom:
    def __init__(self, response_from):
        try:
            self.first_name = response_from.get('first_name').encode('utf-8')
            self.id = response_from.get('id')
            self.username = response_from.get('username').encode('utf-8')

            # print '\t\tTelegramResponseFrom'
            # print '\t\tfirst_name: ' + self.first_name
            # print '\t\tid: ' + str(self.id)
            # print '\t\tusername: ' + self.username
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

#!/usr/bin/env python
# _*_ coding:utf-8 _*

from handlers.ExceptionHandler import ExceptionHandler


class TelegramResponseEntities:
    def __init__(self, entities):
        try:
            self.length = str(entities[0].get('length'))
            self.offset = str(entities[0].get('offset'))
            self.type = str(entities[0].get('type'))

            # print '\t\tResponseEntities'
            # print '\t\tlenght: ' + self.length
            # print '\t\toffset: ' + self.offset
            # print '\t\ttype: ' + self.type
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

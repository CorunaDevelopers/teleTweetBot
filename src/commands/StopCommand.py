#!/usr/bin/env/python
# _*_ coding:utf-8_*_

from handlers.ExceptionHandler import ExceptionHandler


class StopCommand:
    def __init__(self, users):
        self.users = users

    def process_message(self, message):
        try:
            text = message['text']
            if text.startswith('/stop'):
                user_id = message['from']['id']
                user = next((user for user in self.users if user['id'] == user_id), None)
                self.users.remove(user)
                return "¡Ata logo!"
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

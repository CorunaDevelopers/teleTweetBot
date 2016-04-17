#!/usr/bin/env/python
# _*_ coding:utf-8_*_

from handlers.ExceptionHandler import ExceptionHandler


class StopCommand:
    def __init__(self, users):
        # Where's the users?
        # TODO: Do a class to store user domain objects
        self.users = users

    def process_message(self, telegram_response):
        try:
            text = telegram_response.message.text

            if text.startswith('/stop'):
                user_id = telegram_response.message.message_from.id
                # FIX THIS
                user = next((user for user in self.users if user['id'] == user_id), None)
                self.users.remove(user)
                return "¡Ata logo!"
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

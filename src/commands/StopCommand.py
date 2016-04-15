#!/usr/bin/env/python
#_*_ coding:utf-8_*_

class StopCommand:

    def __init__(self, users):
        self.users = users

    def proccess_message(self, message):
        text = message['text']
        if text.startswith('/stop'):
            userId = message['from']['id']
            user = next((user for user in self.users if user['id'] == userId), None)
            self.users.remove(user)
            return "¡Ata logo!"

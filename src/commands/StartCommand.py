#!/usr/bin/env/python
# _*_ coding:utf-8_*_

from handlers.ExceptionHandler import ExceptionHandler


class StartCommand:
    def __init__(self, users):
        self.users = users

    def process_message(self, message):
        try:
            text = message['text']
            if text.startswith('/start'):
                # Guardar el usuario en algun sitio
                user = message['from']
                self.users.append(user)
                return '¡Benvido {0} ! Son o telepaxaro bot, ¡e podo tuitear na rede! Proba a decirme algo para tuitear con /tweet'.format(
                    user['first_name'])
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

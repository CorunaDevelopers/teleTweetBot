#!/usr/bin/env/python
# _*_ coding:utf-8_*_

from handlers.ExceptionHandler import ExceptionHandler


class StartCommand:
    def __init__(self, users):
        self.users = users

    def process_message(self, msg):
        try:
            # text = msg.get('text').encode('utf-8')
            text = msg.message.text
            if text.startswith('/start'):
                # Guardar el usuario en algun sitio
                # raw_user = msg.get('from')
                # self.users.append(user)
                user_first_name = msg.message.message_from.first_name
                self.users.append(msg)
                # return '¡Benvido {0} ! Son o telepaxaro bot, ¡e podo tuitear na rede! Proba a decirme algo para tuitear con /tweet'.format(
                #    user['first_name'])
                return '¡Benvido {0} ! Son o telepaxaro bot, ¡e podo tuitear na rede! Proba a decirme algo para tuitear con /tweet'.format(
                    user_first_name)
        except Exception as ex:
            ExceptionHandler.handle_exception(ex, False)

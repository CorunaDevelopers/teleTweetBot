#!/usr/bin/env/python
# _*_ coding:utf-8_*_

from handlers.ExceptionHandler import ExceptionHandler


# class StartCommand:
#     def __init__(self, users):
#         self.users = users

    # def process_message(self, telegram_response):
    #     try:
    #         text = telegram_response.message.text
    #         if text.startswith('/start'):
    #             # Guardar el usuario en algun sitio
    #             user_first_name = telegram_response.message.message_from.first_name
    #             self.users.append(telegram_response)
    #             return '¡Benvido {0} ! Son o telepaxaro bot, ¡e podo tuitear na rede! Proba a decirme algo para tuitear con /tweet'.format(
    #                 user_first_name)
    #     except Exception as ex:
    #         ExceptionHandler.handle_exception(ex, False)

def process_message(telegram_message):
    try:
        user_id = telegram_message.message.message_from.id
        # TODO: Store the users somewhere
        user_first_name = telegram_message.message.message_from.first_name
        #self.users.append(user_first_name)
        return '¡Benvido {0} ! Son o telepaxaro bot, ¡e podo tuitear na rede! Proba a decirme algo para tuitear con /tweet'.format(user_first_name)
    except Exception as ex:
        ExceptionHandler.handle_exception(ex, False)

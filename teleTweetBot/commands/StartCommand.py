#!/usr/bin/env/python
# _*_ coding:utf-8_*_

from teleTweetBot.handlers.ExceptionHandler import ExceptionHandler


def process_message(telegram_message):
    try:
        # TODO: Store the users somewhere
        # user_id = telegram_message.message.message_from.id
        user_first_name = telegram_message.message.message_from.first_name
        return '¡Benvido {0} ! Son o telepaxaro bot, ¡e podo tuitear na rede! Proba a decirme algo para tuitear con /tweet'.format(
            user_first_name)
    except Exception as ex:
        ExceptionHandler.handle_exception(ex, False)

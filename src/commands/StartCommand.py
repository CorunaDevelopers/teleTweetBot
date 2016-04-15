#!/usr/bin/env/python
#_*_ coding:utf-8_*_

class StartCommand:
    def __init__(self, users):
        self.users = users

    def proccess_message(self, message):
        text = message['text']
        if text.startswith('/start'):
            #Guardar el usuario en algun sitio
            user = message['from']
            self.users.append(user)
            return "¡Benvido " + user['first_name'] + "! Son o telepaxaro bot, ¡e podo tuitear na rede! Proba a decirme algo para tuitear con /tweet"


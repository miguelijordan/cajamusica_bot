# -*- coding: UTF-8 -*-

import telebot
import logging
import cajamusica as cm

# CONSTANTS
TOKEN = "655478604:AAEstqnyDWO-EUDzwpa6AFZmMHPLR0DdssE"

if __name__ == '__main__':
    logging.basicConfig(filename='cajamusica.log', filemode='a+', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',)
    logging.info("La Caja de Música is starting...")

    caja = cm.CajaMusica()
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        logging.info(message)
        bot.send_message(message.chat.id, "Josemi se ha comprado una *caja de música* en la que entra el _sol_ pero no la _luna_, ¿qué más entra en la caja de música?\nUsa el comando /entra para preguntar si una cosa entra en la caja o no.\n¡Sé el primero en llenar la caja de música!", parse_mode="Markdown")

    @bot.message_handler(commands=['entra'])
    def send_botes(message):
        logging.info(message)
        text = message.text
        player = message.from_user
        entra = caja.fit(text)
        if entra:
            bot.reply_to(message, text + " si entra.")
        else:
            bot.reply_to(message, text + " no entra.")

    logging.info("La Caja de Música is running...")
    bot.polling()

# -*- coding: UTF-8 -*-

import telebot
import logging
import cajamusica
import dictionary
import random
import unidecode

# CONSTANTS
TOKEN = ""

if __name__ == '__main__':
    logging.basicConfig(filename='cajamusica.log', filemode='a+', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',)
    logging.info("La Caja de Música is starting...")

    cm = cajamusica.CajaMusica()
    spa_dict = dictionary.Dictionary()
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        logging.info(message)
        bot.send_message(message.chat.id, "Josemi se ha comprado una *caja de música* en la que entra el _sol_ pero no la _luna_, ¿qué más entra en la caja de música?\n" +
        "Usa el comando /entra para preguntar si una cosa entra en la caja o no.\n" +
        "Pídeme pistas con /pista\n" +
        "¡Sé el primero en llenar la caja de música!", parse_mode="Markdown")

    @bot.message_handler(commands=['entra'])
    def send_botes(message):
        logging.info(message)

        original_text = message.text.replace('/entra', '').strip()# ".join(message.text.split()[1:])
        if original_text == "":
            bot.reply_to(message, "Pregúntame por algo: /entra <cosa>")
            return
        text = original_text.lower()
        text = unidecode.unidecode(text)
        player = message.from_user

        entra = cm.fit(text)
        if entra:
            cm.add_word_player(text, player.id)
            bot.reply_to(message, original_text + " si entra.")
            if cm.player_win(player.id):
                cm.remove_player(player.id)
                bot.send_message(message.chat.id, "Enhorabuena " + player.first_name + "!! Has conseguido llenar la caja de música.\n"+
                "¿Has descubierto las reglas que rigen la caja de música o ha sido suerte? "+
                "¿Erez capaz de llenarla de nuevo?", parse_mode="Markdown")
        else:
            cm.remove_player(player.id)
            synonyms = spa_dict.synonyms(text)
            synonyms_entra = list(filter(lambda s: cm.fit(s), synonyms))
            if len(synonyms_entra) > 0:
                s = random.sample(synonyms_entra, 1)[0]
                bot.reply_to(message, original_text + " no entra, pero _" + s + "_ sí entra.", parse_mode="Markdown")
            else:
                bot.reply_to(message, original_text + " no entra.")

    @bot.message_handler(commands=['pista'])
    def send_botes(message):
        logging.info(message)
        bot.reply_to(message, cm.get_pista(), parse_mode="Markdown")

    logging.info("La Caja de Música is running...")
    bot.polling()

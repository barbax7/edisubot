from os import getenv

from flask import Flask, request
from telebot import TeleBot
from telebot.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent, Update, Message)
from telebot import custom_filters

from edisubot.snippets import snip
from edisubot.logs import exception
from edisubot.avvisi import scrape
import re

bot = TeleBot(getenv('BOT_TOKEN'), parse_mode = 'HTML')

app = Flask(__name__)

@app.route("/" + getenv('BOT_TOKEN'), methods = ['POST'])
def getMessage():
    bot.process_new_updates([Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@bot.channel_post_handler(chat_id = [-1001719176635])
def sostituisci_link_con_testo(m: Message):
    
    url: str = re.search(r'https:\/\/\S+', m.text).group(0)
    new = re.sub(r"https:\/\/\S+", f"<a href='{url}'>Leggi l'articolo sul sito EDISU qui.</a>", m.html_text)

    bot.edit_message_text(new, m.chat.id, m.id)

@bot.inline_handler(lambda x: True)
def snipetts(query: InlineQuery):
    
    result = list()
    
    for i in sorted(snip):
        result.append(InlineQueryResultArticle(
            id = i,
            title = i,
            input_message_content = InputTextMessageContent(snip[i], parse_mode = bot.parse_mode),
            description = snip[i]
        ))
    try:
        bot.answer_inline_query(query.id, result)
    except Exception as ex:
        exception(
            "Errore nel fornire le risposte all'utente",
            ex,
            bot,
            getenv('ME'))


bot.add_custom_filter(custom_filters.ChatFilter())



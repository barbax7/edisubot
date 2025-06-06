from os import getenv

from telebot import TeleBot
from telebot.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent, Message)
from telebot import custom_filters

from edisubot.snippets import snip
from edisubot.logs import exception
import re

bot = TeleBot(getenv('BOT_TOKEN'), parse_mode = 'HTML') # type: ignore

@bot.channel_post_handler(chat_id = [getenv('CANALE_AVVISI')])
def sostituisci_link_con_testo(m: Message):

    url: str = re.search(r'https:\/\/\S+', m.text).group(0) # type: ignore
    new = re.sub(r"https:\/\/\S+", f"<a href='{url}'>Leggi l'articolo sul sito EDISU qui.</a>", m.html_text) # type: ignore
    instant = "https://a.devs.today/" + url
    new = "<a href='{}'>‎</a>".format(instant) + new
    bot.edit_message_text(new, m.chat.id, m.id)

@bot.inline_handler(lambda x: True)
def snipetts(query: InlineQuery):
    
    result = list()
    
    for i in sorted(snip):
        result.append(InlineQueryResultArticle(
            id = i,
            title = i,
            input_message_content = InputTextMessageContent(snip[i]['testo'], parse_mode = bot.parse_mode),
            description = snip[i]['testo'],
            reply_markup = snip[i]['markup'] if 'markup' in snip[i].keys() else None
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



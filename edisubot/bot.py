from os import getenv

from flask import Flask, request
from telebot import TeleBot
from telebot.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent, Update)

from edisubot.snippets import snip

bot = TeleBot(getenv('BOT_TOKEN'), parse_mode = 'HTML')

app = Flask(__name__)

@app.route("/" + getenv('BOT_TOKEN'), methods = ['POST'])
def getMessage():
    bot.process_new_updates([Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

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

    bot.answer_inline_query(query.id, result)






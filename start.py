from os import getenv

from edisubot.bot import app, bot
from edisubot.logs import start

if bot.get_webhook_info().url == '': bot.set_webhook(getenv('WEBHOOK'))

start(bot, getenv('ME'))

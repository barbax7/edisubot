from os import getenv

from edisubot.bot import bot
from edisubot.logs import start

start(bot, getenv('ME'))

bot.infinity_polling(
    timeout = 60,
    long_polling_timeout = 5,
    allowed_updates = ['message', 'edited_message', 'channel_post', 'edited_channel_post', 'inline_query', 'chosen_inline_result'],
    skip_pending = True
)
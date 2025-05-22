import logging
import html

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
logging.basicConfig(
    format = '%(asctime)s - (%(filename)s:%(lineno)d) %(levelname)s(%(name)s): %(message)s',
    filename = 'app.log', 
    level = logging.DEBUG)

def start(bot, chatid):
    info_log("Bot avviato", bot, chatid)

def info_log(msg, bot, chatid):
    logger.info(msg)
    bot.send_message(chatid, f"<i>{msg}</i>")

def exception(msg, e, bot, chatid):
    logger.exception(msg)
    bot.send_message(chatid, f"❌ <i>{msg}</i>\n\n<code>{html.escape('|'.join(e.args))}</code>")
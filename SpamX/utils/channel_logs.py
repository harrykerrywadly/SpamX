import html

from SpamX import bot
from SpamX.config import get_int_key
from SpamX.utils.logger import log


async def channel_log(msg, info_log=True):
    chat_id = get_int_key("LOGS_CHANNEL_ID")
    if info_log:
        log.info(msg)

    await bot.send_message(chat_id, html.escape(msg, quote=False))

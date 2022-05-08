import os
import sys
from pyrogram import filters, Client

...

@Client.on_message(filters.command("restart"))
async def restart(bot, message):
    await message.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

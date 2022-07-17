import os
from pyrogram import filters, Client

...

@Client.on_message(filters.command("restart"))
async def restart(bot, message):
    k = await message.reply_text("Restarting...!")
    os.system("python3 -m app")
    await k.edit_text("Restarted Successfully")

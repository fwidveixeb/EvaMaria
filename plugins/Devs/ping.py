import time
import asyncio
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("ping") & filters.user(ADMINS))
async def ping(bot, message):
    try:
        start_time = int(round(time() * 1000))
        k = await message.reply("Processing...")
        end_time = int(round(time() * 1000))
        ping = end_time - start_time
        await k.edit(f"Pong/n {ping}ms")
        
    except Exception as e:
        s = await message.reply(f"#Error {e}")
        await asyncio.sleep(5)
        await s.delete()

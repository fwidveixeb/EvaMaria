import asyncio
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("pin") & filters.user(ADMINS))
async def pin(bot, message):
    
    replied = message.reply_to_message
    
    if replied:
        try:
            await message.delete()
            await replied.delete()
        except Exception as e:
            k = await message.reply(f"#Error {e}")
            await asyncio.sleep(5)
            await k.delete()
            
    if not replied:
        try:
            await message.delete()
        except Exception as e:
            k = await message.reply(f"#Error {e}")
            await asyncio.sleep(5)
            await k.delete()

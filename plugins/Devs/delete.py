import asyncio
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("d") & filters.user(ADMINS))
async def delete(bot, message):
    
    t = message.reply_to_message
    
    if replied:
        try:
            await message.delete()
            await replied.delete()
        except Exception as e:
            k = await message.reply(f"#Error {e}")
            await asyncio.sleep(5)
            await k.delete()
            
    if not replied:
        d

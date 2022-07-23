import asyncio
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("pin") & filters.user(ADMINS))
async def pin(bot, message):
    
    replied = message.reply_to_message
    
    if replied:
        try:
            await message.delete()
            await replied.pin()
    
        except Exception as e:
            k = await message.reply(f"#Error {e}")
            await asyncio.sleep(5)
            await k.delete()
    
    if not replied:
        await message.delete()
        s = await message.reply("Reply to a message to Pin it.")
        await asyncio.sleep(5)
        await s.delete()

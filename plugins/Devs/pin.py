import asyncio
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("pin") & filters.regex(".pin") & filters.user(ADMINS))
async def pin(bot, message):
    
    replied = message.reply_to_message
    
    if replied:
        try:
            await message.delete()
            await replied.pin()
    
        except Exception as e:
            await message.reply(f"#Error {e}")
    
    if not replied:
        await message.delete()
        k = await message.reply("Reply to a message to Pin it.")
        await asyncio.sleep(5)
        await k.delete()
        
@Client.on_message(filters.command("unpin") & filters.regex(".unpin") & filters.user(ADMINS))
async def pin(bot, message):
    
    replied = message.reply_to_message
    
    if replied:
        try:
            await message.delete()
            await replied.unpin()
    
        except Exception as e:
            await message.reply(f"#Error {e}")
    
    if not replied:
        await message.delete()
        k = await message.reply("Reply to a message to Unpin it.")
        await asyncio.sleep(5)
        await k.delete()

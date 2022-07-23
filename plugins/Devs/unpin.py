from info import ADMINS
from pyrogram import Client, filters

Client.on_message(filters.command("unpin") & filters.user(ADMINS))
async def unpin(bot, message):
    
    replied = message.reply_to_message
    
    if replied:
        try:
            await message.delete()
            await replied.unpin()
    
        except Exception as e:
            k = await message.reply(f"#Error {e}")
            await asyncio.sleep(5)
            await k.delete()
    
    if not replied:
        try:
            await message.delete()
            k = await message.reply("Reply to a message to Unpin it.")
            await asyncio.sleep(5)
            await k.delete()
            
        except Exception as e:
            k = await message.reply(f"#Error {e}")
            await asyncio.sleep(5)
            await k.delete()

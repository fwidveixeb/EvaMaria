from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("d") & filters.user(ADMINS))
async def del(bot, message):
  
  replied = message.reply_to_message
  
  if replied:
    await replied.delete()
    await message.delete()
    
  if not replied:
    await message.delete()

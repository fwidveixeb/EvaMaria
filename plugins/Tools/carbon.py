import os
from pyrogram import Client, filters
from plugins.Helper.carbon import Carbon

@Client.on_message(filters.command("carbon"))
async def carbon(bot, message):
  
  carbon = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if replied:
    if replied.document:
        down = await bot.download_media(replied)
        with open(down) as a:
        code = a.read()
      os.remove(down)
    else:
      code = replied.text
    pp = await Carbon(code=code, file_name=f"carbon_{message.chat.id}", backgroundColor="White")
    await message.reply_photo(pp)
    await carbon.delete()
  else: 
    await carbon.edit("Reply to a Text or file")

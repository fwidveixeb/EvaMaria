import os
from pyrogram import Client, filters
from plugins.Helper.carbon import Carbon

@Client.on_message(filters.command("carbon"))
async def carbon(bot, message):
  
  carbon = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if replied:
    if replied.document:
      if replied.document.file_size < 5242880:
        down = await bot.download_media(replied)
        with open(down) as a:
          code = a.read()
          os.remove(down)
      else:
        try:
          code = replied.text
        except:
          return await carbon.edit("File type not supported, Read Help Menu to know how command works.")
    else:
      return await carbon.edit("Reply only to a Text or file, Read Help Menu to know how command works.")
    pp = await Carbon(code=code, file_name=f"carbon_{message.chat.id}", backgroundColor="White")
    await message.reply_photo(pp)
    await carbon.delete()
  else: 
    await carbon.edit("Reply only to a Text or file, Read Help Menu to know how command works.")

import os
import random
from . import *
from carbonnow import Carbon
from pyrogram import Client, filters

@Client.on_message(filters.command("carbon"))
async def carbon(bot, message):
  
  replied = message.reply_to_message
  
  abcd = await message.reply("Processing...")
  if replied:
      if replied.media:
          b = await bot.download_media(replied)
          a = open(b)
          code = a.read()
          a.close()
          os.remove(b)
      else:
          code = replied.text
  else:
      code = replied.text.split(" ", maxsplit=1)[1]
  carbon = Carbon(code=code)
  ab = await carbon.save("hagadmansa_carbon")
  await abcd.delete()
  await bot.send_photo(message.chat.id, ab, caption=f"Carbonised by {message,from_user.mention}")
  os.remove(xx)

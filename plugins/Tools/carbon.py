import os
import random
from pyrogram import Client, filters
from plugins.Helper.carbon import Carbon

colorpath = "resources/colorlist.txt"

if os.path.exists(colorpath):
 with open(colorpath, "r") as f:
  colors = f.read().split()
else:
 colors = []

rom = random.choice(colors)

@Client.on_message(filters.command("carbon"))
async def carbon(bot, message):
  
  carbon = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if len(message.command) == 1:
     bg = "White"
  elif message.command[1] in ["random", "Random"]:
     bg = rom
  else:
     bg = message.command[1]
  
  if replied.text:
     code = replied.text
     pp = await Carbon(code=code, file_name=f"carbon_{message.chat.id}", backgroundColor=bg)
     await message.reply_photo(pp)
     await carbon.delete()
      
  elif replied.document:
     if replied.document.file_size > 5242880:
        return await carbon.edit("Replied file must be less then 5 Mb.")
     try:
        down = await bot.download_media(replied)
        with open(down) as a:  
           code = a.read()
           os.remove(down)
     except:
        return await carbon.edit("Reply only to a Text file only, Read Help Menu to know how command works.")
     pp = await Carbon(code=code, file_name=f"carbon_{message.chat.id}", backgroundColor=bg)
     await message.reply_photo(pp)
     await carbon.delete()
  else:
     return await carbon.edit("Reply only to a Text or file, Read Help Menu to know how command works.")

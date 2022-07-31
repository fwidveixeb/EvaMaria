import os
import random
from pyrogram import Client, filters
from plugins.Helper.carbon import Carbon

colorpath = "resources/colorlist.txt"

with open(colorpath, "r") as f:
  colors = f.read().split()

rom = random.choice(colors)

@Client.on_message(filters.command("carbon"))
async def carbon(bot, message):
  
  carbon = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if len(message.command) == 1:
     bg = "White"
  elif len(message.command) == 2 and message.command[1] in ["random", "Random"]:
     bg = rom
  elif len(message.command) == 2 and message.command[1] in ["colorlist", "Colorlist"]:
     await message.reply_document(
      document="resources/colorlist.txt",
      caption="Here is the list of colors for Command Carbon.",
      thumb="resources/devoloper.png"
     )
  else:
     bg = message.command[1]
    
  if not replied:
     return await carbon.edit("Reply only to a Text or file, Read Help Menu to know how command works.")
  
  elif replied.text:
     code = replied.text
     pp = await Carbon(code=code, file_name=f"carbon_{message.chat.id}", backgroundColor=bg)
     await message.reply_photo(pp)
     await carbon.delete()
      
  else replied.document:
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

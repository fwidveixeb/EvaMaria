import os
import random
from pyrogram import Client, filters
from plugins.Helper.carbon import Carbon

@Client.on_message(filters.command("carbon"))
async def carbon(bot, message):
  
  carbon = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  colorpath = "resources/colorlist.txt"
  with open(colorpath, "r") as f:      
     colors = f.read().split()
  rom = random.choice(colors)
  
  if len(message.command) == 1:
     bg = "White"
  elif len(message.command) == 2 and message.command[1] in ["random", "Random"]:
     bg = rom
  elif len(message.command) == 2 and message.command[1] in ["colorlist", "Colorlist"]:
     return await carbon.edit("[Here](https://telegra.ph/List-of-Colors-07-31) is the list of Colors.")
  else:
     bg = message.command[1]
    
  if not replied:
     return await carbon.edit("Reply to a Text or file, Read Help Menu to know how command works.")
  
  if replied.text:
     code = replied.text
     pp = await Carbon(code=code, file_name=f"carbon_{message.chat.id}", backgroundColor=bg)
     await message.reply_photo(photo=pp, caption=f"Here is your Carbonized Image with `{bg}` color.")
     return await carbon.delete()
      
  if replied.document:
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
     await message.reply_photo(photo=pp, caption=f"Here is your Carbonized Image with `{bg}` color.")
     return await carbon.delete()
  await carbon.edit("Reply only to a Text or file, Read Help Menu to know how command works.")

import os
import random
from pyrogram import Client, filters
from plugins.Helper.carbon import Carbon

colopath = "resources/colorlist.txt"

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
  
  if replied:
    if replied.document:
      if replied.document.file_size > 5242880:
        return await carbon.edit("Replied file must be less then 5 Mb.")
      try:
        down = await bot.download_media(replied)
        with open(down) as a:
          code = a.read()
          os.remove(down)
      except:
        return await carbon.edit("Reply to a text file only, Read Help Menu to know how command works.")
    else:
      code = replied.text
    if len(message.command) == 1:
      bg = "White"
    elif len(message.command) == 2 and message.command[1] in ["random", "Random"]:
      bg = rom
    elif len(message.command) == 2 and len(message.command[1]) == 6:
      bg = message.command[1]
    elif len(message.command) > 2:
     return await carbon.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  
    elif:
      return await carbon.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [132 FIRST_PARAMETER_INVALID] - Firet Parameter should be 'Random' if need random colors, otherwise it should be a combination of 6 alphabets and numbers if need custom colors (Caused by 'Argument.ValueError')`")
    pp = await Carbon(code=code, file_name=f"carbon_{message.chat.id}", backgroundColor=bg)
    await message.reply_photo(pp)
    await carbon.delete()
  else: 
    await carbon.edit("Reply only to a Text or file, Read Help Menu to know how command works.")

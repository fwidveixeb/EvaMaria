import os
from pyrogram import Client, filters
from plugins.Helper.phlogo import generate

@Client.on_message(filters.command("ph"))
async def phlogoph(bot, message):
  
  ph = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await ph.edit("No Text Provided to make PornHub logo, Read Help Menu to know how command work.")
  
  elif len(message.command) == 2:
    return await ph.edit("Provide 2 text to make PornHub logo.")
  
  elif len(message.command) == 3:
    first = message.command[1]
    second = message.command[2]
    logo = generate(first, second)
    name = f"phlogo_{message.chat.id}.png"
    logo.save(name)
    await message.reply_photo(name)
    await ph.delete()
    os.remove(name)
  else:
    await ph.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  

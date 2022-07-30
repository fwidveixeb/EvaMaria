import os
from pyrogram import Client, filters
from plugins.Helper.bash import bash

@Client.on_message(filters.command("glitch"))
async def glitch(bot, message):
  
  glitch = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if not replied:
    return await glitch.edit('Reply to a photo to convert it to Glitch')
  
  elif replied.photo
    await bash("pip install -e git+https://github.com/1Danish-00/glitch_me.git#egg=glitch_me")
    poma = await bot.download_media(replied)
    cmd = f"glitch_me gif --line_count 200 -f 10 -d 50 '{poma}' glitch_{message.chat.id}_.gif"
    stdout, stderr = await bash(cmd)
    await message.reply_animation(f"glitch_{message.chat.id}_.gif")
    await glitch.delete()
    os.remove(poma)
    os.remove(f"glitch_{message.chat.id}_.gif")
    
  else: 
    await glitch.edit('Reply to a photo only.')

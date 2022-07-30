import os
from pyrogram import Client, filters
from plugins.Helper.bash import bash

@Client.on_message(filters.command("glitch"))
async def glitch(bot, message):
  
  glitch = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if not replied:
    return await glitch.edit('Reply to a photo to convert it to Glitch')
  
  elif replied.photo:
    poma = await bot.download_media(replied)
    userid = message.chat.id
    cmd = f"glitch_me gif --line_count 200 -f 10 -d 50 '{poma}' glitch_{userid}_.gif"
    stdout, stderr = await bash(cmd)
    await message.reply_animation(f"glitch_{userid}_.gif")
    await glitch.delete()
    os.remove(poma)
    os.remove(f"glitch_{userid}_.gif")
    
  else: 
    await glitch.edit('Reply to a photo only.')

import os
from PIL import Image
from pyrogram import Client, filters

@Client.on_message(filters.command("size"))
async def suze(bot, message):
  
  size = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if replied.photo: 
    img = bot.download_media(replied)
    im = Image.open(img)
    x, y = im.size
    await size.edit(f"Dimension of the Image is `{x} x {y}`")
    os.remove(img)
  else: 
    await size.edit("Reply to a photo only.")

import os
import png
import pyqrcode
from pyqrcode import QRCode
from pyrogram import Client, filters

def listToString(s):
    str1 = " "
    return (str1.join(s))

@Client.on_message(filters.command("qrcode"))
async def qrdoce(bot, message):
  
  if len(message.command) == 1:
    return await message.reply("No Text provided, Read Help Menu to know how command works.")

  qr = await message.reply("`Processing...`")
  replied = message.reply_to_message
    
  if replied.text:
    komal = replied.text.split()
    final = listToString(komal)
  else: 
    id = message.chat.id
    txt = message.command[1:]
    final = listToString(txt)
  
  try:
      pyqrcode.create(final).png(f"qr_code_{id}.png" , scale = 6)
      await message.reply_photo(f"qr_code_{id}.png")
      await qr.delete()
      os.remove(f"qr_code_{id}.png")
  except Exception as e:
      await qr.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`{e}`")
      os.remove(f"qr_code_{id}.png")
  

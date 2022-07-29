import os
import png
import pyqrcode
from pyqrcode import QRCode
from pyrogram import Client, filters

@Client.on_message(filters.command("qrcode"))
async def qrdoce(bot, message):
  
  if len(message.command) == 1:
    return await message.reply("No URL or Text provided, Read Help Menu to know how command works.")
  
  qr = await message.reply("`Processing...`")
  id = message.chat.id
  url = message.command[1:]
  
  try:
      pyqrcode.create(url).png(f"qr_code_{id}.png" , scale = 6)
      await message.reply_photo(photo=f"qr_code_{id}.png", caption=f"Here is your QR Code for {url}")
      await qr.delete()
      os.remove(f"qr_code_{id}.png")
  except Exception as e:
      await qr.edit(f"#Error {e}, foreard this to @HagadmansaChat")
      os.remove(f"qr_code_{id}.png")
  

import os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("tpdne"))
async def tpdne(bot, message):
  tpdne = await message.reply("processing...")
  URL = "https://thispersondoesnotexist.com/image"
  response = requests.get(URL)
  open("tpdne.jpg", "wb").write(response.content)
  await message.reply_photo("tpdne.jpg")
  await tpdne.delete()
  os.remove("tpdne.jpg")

import os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("tpdne"))
async def tpdne(bot, message):
  id = message.chat.id
  tpdne = await message.reply("`Processing...`")
  URL = "https://thispersondoesnotexist.com/image"
  response = requests.get(URL)
  open(f"tpdne_{id}.jpg", "wb").write(response.content)
  await message.reply_photo(f"tpdne_{id}.jpg")
  await message.reply_document(f"tpdne_{id}.jpg")
  await tpdne.delete()
  os.remove(f"tpdne_{id}.jpg")

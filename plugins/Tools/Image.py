import os
import cv2
import asyncio
import numpy as np
from PIL import Image
from validators.url import url
from pyrogram import Client, filters
from telegraph import upload_file as upf

@Client.on_message(filters.command("color"))
async def color(bot, message):
  replied = message.reply_to_message
  if not replied.media:
      return await message.reply("Reply to a Black & White Image to color it")
  xx = await message.reply("Coloring image 🎨🖌️...") 
  image = await bot.download_media(replied.media)
  img = cv2.VideoCapture(image)
  ret, frame = img.read()
  cv2.imwrite("hagadmansa.jpg", frame)
  key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
  r = requests.post(
      "https://api.deepai.org/api/colorizer",
      files={"image": open("hagadmansa.jpg", "rb")},
      headers={"api-key": key},
  )
  os.remove("hagadmansa.jpg")
  os.remove(image)
  r_json = r.json()["output_url"]
  await bot.send_photo(chat_id=message.chat.id, photo=r_json, caption="Successfully filled colour in Image 🎨🖌")
  await xx.delete()

import os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("picsum"))
async def picsum(bot, message):
    
  if len(message.command) == 1:
    await message.reply("No size details provided, Read Help Menu First.")
    
  if len(message.command) == 2:
    await message.reply("Who will provide width?")
    
  elif len(message.command) == 3:
    picsum = await message.reply("processing")
    height = message.command[2]
    width = message.command[3]
    API = "https://picsum.photos"
    response = requests.get(f"{API}/{width}/{height}")
    open("picsum.jpg", "wb").write(response.content)
    await message.reply_photo("picsum.jpg")
    await picsum.delete()
    os.remove("picsum.jpg")
    
  else:
    await message.reply("Something went wrong")

import os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("picsum"))
async def picsum(bot, message):
  
  if not message.command:
    await message.reply("No arguments provided, Read Help menu first")
    
  elif (message.command) == 1:
    await message.reply("Required 2 arguments, you provided only 1.")
    
  elif (message.command) == 2:
    picsum = await message.reply("processing")
    height = message.command[1]
    width = message.command[2]
    API = "https://picsum.photos"
    response = requests.get(f"{API}/{width}/{height}")
    open("picsum.jpg", "wb").write(response.content)
    await message.reply_photo("picsum.jpg")
    await picsum.delete()
    os.remove("picsum.jpg")
    
  else:
    await message.reply("Something went wrong")

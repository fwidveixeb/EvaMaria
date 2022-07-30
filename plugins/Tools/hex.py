import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("hex"))
async def hex(bot, message):
  
  hex = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await hex.edit("No color code provided, Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
    color = message.command[1]
    if len(color) == 6:
      photo = requests.get(f"https://da.gd/image/750*750/jpg?bgcolor={color}")
      await message.reply_photo(photo=photo, caption=f"Here is the Image for Hex Color `{color}`.")
      await hex.delete()
    else:
      hex.edit("Color code must be a combination of 6 alphabets & numbers.") 
  else:
    await hex.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  

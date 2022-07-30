import requests
from pyrogram import Client, filters
from plugins.Helper.url_checker import is_url_ok

@Client.on_message(filters.command("dagd"))
async def dagd(bot, message):
  
  dagd = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await dagd.edit("No URL provided to short, Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
    url = message.command[1]
    if not is_url_ok(url):
      return await dagd.edit("Invalid URL Provided.")
    response = requests.get(f"https://da.gd/s?url={url}").text
    await dagd.edit(f"{response}")
  else:
    await dagd.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  

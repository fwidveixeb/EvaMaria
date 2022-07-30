import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("dns"))
async def dns(bot, message):
  
  dns = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await dns.edit("No Server provided to check DNS, Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
    url = message.command[1]
    xurl = url.split('/')
    final = xurl[2]
    response = requests.get(f"https://da.gd/dns/{final}").text
    await dns.edit(f"`{response}`")
  else:
    await dns.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  

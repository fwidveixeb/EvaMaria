import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("bully"))
async def bully(bot, message):
  k = await message.reply("processing...")
  API = "https://api.safone.tech/bully"
  m = requests.get(f"{API}").json()
  n = m['bully']
  o = f"{n}"
  await k.edit(f"{o}")
  

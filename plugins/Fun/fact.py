import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("fact"))
async def fact(bot, message):
  k = await message.reply("processing...")
  API = "https://api.safone.tech/fact"
  m = requests.get(f"{API}").json()
  n = m['fact']
  await k.edit(f"{n}")
  

import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("joke"))
async def joke(bot, message):
  k = await message.reply("processing...")
  API = "https://api.safone.tech/joke"
  m = requests.get(f"{API}").json()
  n = m['joke']
  await k.edit(f"{n}")
  

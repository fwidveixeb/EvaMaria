import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("quote"))
async def quote(bot, message):
  k = await message.reply("processing...")
  API = "https://api.safone.tech/quote"
  m = requests.get(f"{API}").json()
  n = m['quote']
  o = f"{n}   ~**{message.from_user.mention}**"
  await k.edit(f"{o}")
  

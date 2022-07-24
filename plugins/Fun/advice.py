import requests
from pyrogram import Clienr, filters

@Client.on_message(filters.command("advice"))
async def advuce(bot, message):
  k = await message.reply("processing...")
  API = "https://api.safone.tech/advice"
  m = requests.get(f"{API}").json()
  n = m['advice']
  o = f"{m} **-{message.from_user.mention}**"
  await k.edit(f"{o}")
  

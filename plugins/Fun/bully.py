import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("bully"))
async def bully(bot, message):
  
  bully = await message.reply("`Processing...`")
  API = "https://api.safone.tech/bully"
  try:
    m = requests.get(f"{API}").json()
    n = m['bully']
    await bully.edit(f"{n}")
  except Exception as e:
    await bully.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
  
  

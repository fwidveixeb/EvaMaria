import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("fact"))
async def fact(bot, message):
  
  fact = await message.reply("`Processing...`")
  API = "https://api.safone.tech/fact"
  try:
    m = requests.get(f"{API}").json()
    n = m['fact']
    await fact.edit(f"{n}")
  except Exception as e:
    await fact.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")

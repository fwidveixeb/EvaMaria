import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("dare"))
async def dare(bot, message):
  
  dare = await message.reply("`Processing...`")
  API = "https://api.safone.me/dare?category=classic"
  try:
    m = requests.get(f"{API}").json()
    n = m['dare']
    await dare.edit(f"{n}")
  except Exception as e:
    await dare.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")

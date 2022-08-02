import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("joke"))
async def joke(bot, message):
  
  joke = await message.reply("`Processing...`")
  API = "https://api.safone.tech/joke"
  try:
    m = requests.get(f"{API}").json()
    n = m['joke']
    await joke.edit(f"{n}")
  except Exception as e:
    await joke.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")

import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("truth"))
async def truth(bot, message):
  
  truth = await message.reply("`Processing...`")
  API = "https://api.safone.tech/truth?category=classic"
  try:
    m = requests.get(f"{API}").json()
    n = m['truth']
    await truth.edit(f"{n}")
  except Exception as e:
    await truth.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")

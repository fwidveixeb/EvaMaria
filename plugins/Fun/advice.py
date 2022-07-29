import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("advice"))
async def advice(bot, message):
  
  advice = await message.reply("`Processing...`")
  API = "https://api.safone.tech/advice"
  try:
    m = requests.get(f"{API}").json()
    n = m['advice']
    o = f"{n}   ~**{message.from_user.first_name} {message.from_user.last}**"
    await advice.edit(f"{o}")
  except Exception as e:
    await advice.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
  
  

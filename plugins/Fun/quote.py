import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("advice"))
async def quote(bot, message):
  
  quote = await message.reply("`Processing...`")
  API = "https://api.safone.tech/quote"
  try:
    m = requests.get(f"{API}").json()
    n = m['quote']
    o = f"{n}   ~**{message.from_user.first_name} {message.from_user.last_name}**"
    await quote.edit(f"{o}")
  except Exception as e:
    await quote.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
  
  

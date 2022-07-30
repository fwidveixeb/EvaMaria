import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("decide"))
async def decide(bot, message): 
  k = requests.get("https://yesno.wtf/api").json()
  ans = k['answer']
  gif = k['image']
  answer = ans.capitalize()
  await message.reply_animation(animation=gif, caption=answer)

import calendar
from datetime import datetime as dt
from pyrogram import Client, message

@Client.on_message(filters.command("date"))
async def date(bot, message):
  
  date = await message.reply("`Processing...`")
  
  m = dt.now().month   
  y = dt.now().year
  d = dt.now().strftime("Date - %B %d, %Y\nTime- %H:%M:%S")
  k = calendar.month(y, m)
  await date.edit(f"`{k}\n{d}`")

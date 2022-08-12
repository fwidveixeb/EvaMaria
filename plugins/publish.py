from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command('publish') & filters.user(ADMINS))
async def publish(bot, message):
  
  #pb = await message.reply("`Processing...`")
  
  # Getting message ids
  a =  message.id - 8
  b = message.id - 6
  c = message.id - 3
  d = message.id - 1
  
  # Finding text from message ids
  e = await bot.get_messages(message.chat.id, a)
  f = await bot.get_messages(message.chat.id, b)
  g = await bot.get_messages(message.chat.id, c)
  h = await bot.get_messages(message.chat.id, d)
 
  await message.reply(e.text)
  await message.reply(f.text)
  await message.reply(g.text)
  await message.reply(h.text)

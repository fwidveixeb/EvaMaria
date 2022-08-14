from bot import bot
from info import ADMINS
from pyromod import listen
from pyrogram import Client, filters

@Client.on_message(filters.command('hello') & filters.user(ADMINS))
async def genStr(bt, message):
  
  one = await bot.ask(message.chat.id, "send me a file.")
  await message.reply_cached_media(one.document.file_id)
  
  two = await bot.ask(message.chat.id, "Now send me the Text")
  await message.reply_cached_media(two.text)
  

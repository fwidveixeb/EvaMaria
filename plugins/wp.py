from bot import bot
from info import ADMINS
from pyromod import listen
from pyrogram import Client, filters

@bot.on_message(filters.private & filters.document & filters.user(ADMINS))
async def genStr(bt, message):
  
  one = await bt.get_messages(message.chat.id, message.id)
  await message.reply_cached_media(one.document.file_id)
  
  two = await bot.ask(message.chat.id, "Now send me second document.")
  await message.reply_cached_media(two.document.file_id)
  
if __name__ == "__main__":
    bot.run()

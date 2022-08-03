from pyrogram import Client, filters

@Client.on_message(filters.command("send"))
async def user(bot, message):
  file = message.command[1]
  await message.reply_cached_media(file)

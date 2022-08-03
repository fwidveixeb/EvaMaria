from pyrogram import Client, filters

@Client.on_message(filters.command("send"))
async def user(bot, message):
  file = message.command[1]
  await message.reply_cached_media(file)

@Client.on_message(filters.command("file"))
async def file(bot, message):
    print(message.reply_to_message.document.file_id)
    await message.reply(message.reply_to_message.document.file_id)

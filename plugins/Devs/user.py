from pyrogram import Client, filters

@Client.on_message(filters.command("send"))
async def user(bot, message):
  file = message.command[1]
  await message.reply_cached_media(file)

@Client.on_message(filters.command("file"))
async def file(bot, message):
    replied = message.reply_to_message
    media = replied.document or replied.video or replied.photo
    k = replied.file_id
    print(k)
    await message.reply(k)

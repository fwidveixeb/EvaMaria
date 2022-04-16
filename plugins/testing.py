from pyrogram import Client, filters

@Client.on_message(filters.document & filters.private)
async def document(bot, message):
  await message.reply(message.document.file_id)

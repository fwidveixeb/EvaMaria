from pyrogram import Client, filters

@Client.on_message(filters.document & filters.private)
def document(bot, message):
  message.reply(message.document.file_id)

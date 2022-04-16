from pyrogram import Client, filters

@Client.on_message(filters.command('docs'))
def document(bot, message):
  bot.send_document(message.chat.id, "BQACAgQAAx0CXHCEYQACBPBiIvV5YpuV9LuD7wUKr42XMz1D1gACyAkAAnftCVMZyZfmh1asvR4E")

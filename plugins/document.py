from pyrogram import Client, filters

@Client.on_message(filters.command("abcd"))
async def kdneidhd(bot, message):
  
  replied = message.reply_to_message
  
  if replied.document:
    s = await bot.download_media(message=replied, file_name=f"{message.chat.id}.txt")
    k = open(f"{message.chat.id}.txt")
    p = k.read()
    await message.reply(f"{p}")
    k.close()
    

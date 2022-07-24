from pyrogram import Client, filters

@Client.on_message(filters.command("abcd"))
async def kdneidhd(bot, message):
  
  replied = message.reply_to_message
  
  if replied.document:
    path = (f"./DOWNLOADS/{message.chat.id}.txt")
    s = await bot.download_media(message=replied, file_name=path)
    k = open(path)
    p = k.read()
    await message.reply(f"{p}")
    k.close()
    

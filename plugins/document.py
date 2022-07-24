from pyrogram import Client, filters

@Client.on_message(filters.command("abcd"))
async def kdneidhd(bot, medsage):
  
  replied = message.reply_to_message
  
  if replied.document:
    s = await bot.download_media(media=replied)
    k = open('s')
    p = k.read()
    await message.reply(f"{p}")
    k.close()
    

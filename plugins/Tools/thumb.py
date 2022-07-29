"""from pyrogram import Client, filters

@Client.on_message(filters.command("thumb"))
async def thumb(bot, message):
  
  thumb = await message.reply("`Processing...`")
  replied = message.reply_to_message

  if not replied & replied.document:
    return await thumb.edit("Reply to a file to download it's Thumbnail.")
  
  if not replied.document.thumbs:
    return await thumb.edit("Replied file has no Thumbnail to show.")

  await replied.download_media(thumb=-1)
  m = await reply_photo(m)
  os.remove(m)"""

from pyrogram import Client, filters

@Client.on_message(filters.command("ul") & filters.user(ADMINS))
async def ul(bot, message):
  
  ul = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await ul.edit('`No path given to upload.`')
  
  else:
    lama = message.command[1:]
    
  try:
    await message.reply_document(
    document=lama,
    thumb="resources/devoloper.png"
    )
  except:
    return await ul.edit('`Either the Directory is empty or Incorrect.`')

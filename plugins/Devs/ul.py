import time
from info import ADMINS
from pyrogram import Client, filters
from plugins.Helper.progress import progress

@Client.on_message(filters.command("ul") & filters.user(ADMINS))
async def ul(bot, message):

  ul = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await ul.edit('`No path given to upload.`')
  
  else:
    lama = message.command[1]
    
  try:
    hemlo = await message.reply_document(
    document=lama,
    thumb="resources/devoloper.png",
    progress=progress
    )
    await ul.delete()
    await hemlo.edit(f"Successfully uploaded `{lama}`.")
  except:
    return await ul.edit('`Either the Directory is empty or Incorrect.`')

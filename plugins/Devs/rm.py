import os
import time
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("rm") & filters.user(ADMINS))
async def rm(bot, message):

  rm = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await rm.edit('`No path given to remove.`')
  
  else:
    suar = message.command[1]
    
  try:
    os.remove(suar)
    await rm.delete()
    await hemlo.edit(f"Successfully removed `{suar}`.")
  except:
    return await rm.edit('`Either the Directory is empty or Incorrect.`')

import os
import time
from info import ADMINS
from pyrogram import Client, filters 
from plugins.Helper.progress import progress

def listToString(s):
  str1 = " "
  return (str1.join(s))
  
@Client.on_message(filters.command('rename'))
async def rename(bot, message):
  
    rn = await message.reply(text="`Processing...`", reply_to_message_id=message.reply_to_message.id)
    replied = message.reply_to_message
    
    if (" " in message.text) and (replied is not None):
      
        filename = message.command[1:]
        file_name = listToString(filename)
        
        time_ = time.time()
        the_real_download_location = await bot.download_media(
            message=replied,
            progress=progress,
            progress_args=(f'**Name:** `{file_name}`\n**Status:** Downloading...', rn, time_)
        )
 
        os.rename(the_real_download_location, file_name)
            
        time_ = time.time()
        await message.reply_document(
            document=file_name,
            thumb='resources/devoloper.png',
            caption=file_name,
            progress=progress,
            reply_to_message_id=message.reply_to_message.id,
            progress_args=(f'**Name:** `{file_name}`\n**Status:** Uploading...', rn, time_)
        )
        os.remove(file_name)
        await rn.delete()
    else:
        await rn.edit('Reply to file and provide a new name.')
    

import os
import time
import traceback
from pyrogram import Client, filters 
from plugins.Helper.progress import progress

def listToString(s):
  str1 = " "
  return (str1.join(s))
  
@Client.on_message(filters.command('rx'))
async def rename(bot, message):
  
  try:
  
    if message.from_user.id not in [1250003833, 5099088450]:
        return
  
    rn = await message.reply(text="`Processing...`", reply_to_message_id=message.reply_to_message.id)
    replied = message.reply_to_message
    
    if (" " in message.text) and (replied is not None):
     
        file_name = message.caption.split('|')[0]
        caption = message.caption.split('|')[1]
        
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
            caption=caption,
            progress=progress,
            reply_to_message_id=message.reply_to_message.id,
            progress_args=(f'**Name:** `{file_name}`\n**Status:** Uploading...', rn, time_)
        )
        os.remove(file_name)
        await rn.delete()
    else:
        await rn.edit('Reply to file and provide a new name.')
  except Exception as e:
        txt = traceback.format_exc() 
        return await rn.edit(f"**Traceback Info:**\n`{txt}`\n**Error Text:**\n`{e}`")
    

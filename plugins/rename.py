import os
import time
from info import ADMINS
from pyrogram import Client, filters 
from plugins.Helper.progress import progress
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command('rename') & filters.user(ADMINS))
async def rename(bot, message):
  
    rn = await message.reply("`Processing...`")
    
    if (" " in message.text) and (update.reply_to_message is not None):
        cmd, file_name = message.text.split(" ", 1)
        if len(file_name) > 128:
            return await rn.edit('File name can not be longer then 128.')
        
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=message.reply_to_message,
            progress=progress
            progress_args=('Downloading to my server', rn, c_time)
        )
        if the_real_download_location is not None:
            try:
                await rn.edit('Read line 26.')
            except:
                pass
            os.rename(the_real_download_location, file_name)
            await rn.edit('Uploading to Telegram')
            
            c_time = time.time()
            await message.reply_document(
                document=file_name,
                thumb='resources/devoloper.png',
                caption=file_name,
                progress=progress,
                progress_args=('Uploading...', rn, c_time)
            )
            try:
                os.remove(file_name)
            except:
                pass
            await rn.edit('Successfully Uploaded')
    else:
        await rn.edit('Reply to file and provide a new name')
    

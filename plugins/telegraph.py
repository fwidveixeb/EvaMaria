import os
from pyrogram import Client, filters
from telegraph import upload_file

@Client.on_message(filters.command("telegraph"))
async def telegraph(bot, message):
    
    replied = message.reply_to_message
    
    if replied.photo:
        p = await message.reply("Downloading...")
        user_id = str(message.chat.id)
        file_name_ = (f"./DOWNLOADS/{user_id}.jpg")
        download = await bot.download_media(message=replied, file_name=file_name_)
        await p.edit("Uploading...")
        try:         
            tgraph_link = upload_file(download)
            await p.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_link[0]}")     
            os.remove(download) 
        except Exception as e:
            await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
                
            
            
                                     
  
  
  
  
  
  

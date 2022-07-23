import os
from pyrogram import Client, filters
from telegraph import upload_file

@Client.on_message(filters.command("telegraph"))
async def telegraph(bot, message):
    
    replied = message.reply_to_message
    
    if replied.photo:
        p = await message.reply("Downloading...")
        user_id = str(message.chat.id)
        img_path = (f"./DOWNLOADS/{user_id}.jpg")
        img_download = await bot.download_media(message=replied, file_name=img_path)
        await p.edit("Uploading...")
        try:         
            tgraph_img = upload_file(img_download)
            await p.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_img[0]}", disable_web_page_preview=True)     
            os.remove(img_download) 
        except Exception as e:
            await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            
    elif replied.video:
        if replied.video.file_size < 5242880:
            a = await message.reply_text("Downloading...")
            user_id = str(message.chat.id)
            vid_path = (f"./DOWNLOADS/{user_id}.mp4")
            vid_download = await bot.download_media(message=replied, file_name=vid_path)
            await a.edit("Uploading...")
            try:
                tgraph_vid = upload_file(vid_download)
                await a.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_vid[0]}", disable_web_page_preview=True)     
                os.remove(vid_download) 
            except Exception as e:
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
            
    elif replied.animation:
        if replied.animation.file_size < 5242880:
            g = await message.reply("Downloading...")
            user_id = str(message.chat.id)
            gif_path = (f"./DOWNLOADS/{user_id}.mp4")
            gif_download = await bot.download_media(message=replied, file_name=gif_path)
            await g.edit("Uploading...")
            try:
                tgraph_gif = upload_file(vid_download)
                await g.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_gif[0]}", disable_web_page_preview=True)     
                os.remove(gif_download) 
            except Exception as e:
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
        
            
   

import os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("picsum"))
async def picsum(bot, message):
    
    r = message.text.split(None)
    
    if len(message.command) == 1:
        await message.reply("No size details provided, Read Help Menu First.")
    
    elif len(message.command) == 2:
        await message.reply("Who will provide width?")
    
    elif len(r) > 2:
        picsum = await message.reply("processing")
        height = message.text.split(None, 2)[1]
        width = message.text.split(None, 2)[2]
        API = "https://picsum.photos"
        try:
            response = requests.get(f"{API}/{height}/{width}")
            open("picsum.jpg", "wb").write(response.content)
            await message.reply_photo("picsum.jpg")
            await picsum.delete()
            os.remove("picsum.jpg")
        except Exception as e:
            await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**OUTPUT:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Forward this to @HagadmansaChat.__")
            os.remove("picsum.jpg")
    
    elif len(r) > 3:
        picsum = await message.reply("processing")
        height = message.text.split(None, 3)[1]
        width = message.text.split(None, 3)[2]
        grayscale = message.text.split(None, 3)[3]
        if grayscale != "True":
         retu   await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**OUTPUT:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Third argument must be 'blur', except ''.\n4. Forward this to @HagadmansaChat.__") 
        API = "https://picsum.photos"
        try:
            response = requests.get(f"{API}/{height}/{width}?{blur}")
            open("picsum.jpg", "wb").write(response.content)
            await message.reply_photo("picsum.jpg")
            await picsum.delete()
            os.remove("picsum.jpg")
        except Exception as e:
            await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**OUTPUT:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Forward this to @HagadmansaChat.__")
            os.remove("picsum.jpg")
    else:
        await message.reply("Something went wrong")

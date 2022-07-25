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
    
    elif len(r) == 3:
        API = "https://picsum.photos"
        picsum = await message.reply("processing")
        height = message.text.split(None, 2)[1]
        width = message.text.split(None, 2)[2]
        try:
            response = requests.get(f"{API}/{height}/{width}")
            open("picsum.jpg", "wb").write(response.content)
            await message.reply_photo("picsum.jpg")
            await picsum.delete()
            os.remove("picsum.jpg")
        except Exception as e:
            await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**OUTPUT:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Forward this to @HagadmansaChat.__")
            os.remove("picsum.jpg")
    
    elif len(r) == 4:
        API = "https://picsum.photos"
        picsum = await message.reply("processing")
        height = message.text.split(None, 3)[1]
        width = message.text.split(None, 3)[2]
        third = message.text.split(None, 3)[3]
        
        if third == "True":
            try:     
                response = requests.get(f"{API}/{height}/{width}?grayscale")
                open("picsum.jpg", "wb").write(response.content)
                await message.reply_photo("picsum.jpg")
                await picsum.delete()
                os.remove("picsum.jpg")
            except Exception as e:
                await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**OUTPUT:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Pass 'True' in thirt argument to get a Black & White Image.\n4. Forward this to @HagadmansaChat.__")
                os.remove("picsum.jpg")
                
        elif third == 10 or third == 9 or third == 8 or third == 7 or third == 6 or third == 5 or third == 4 or third == 3 or third == 2 or third == 1:
            try:     
                response = requests.get(f"{API}/{height}/{width}?blur={third}")
                open("picsum.jpg", "wb").write(response.content)
                await message.reply_photo("picsum.jpg")
                await picsum.delete()
                os.remove("picsum.jpg")
            except Exception as e:
                await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**OUTPUT:**\n`Third argument must be equal to 'True' if need a Black & White Image or must be from 1 to 10 to get a blur Image.`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Pass a integer value between 1 to 10 to get blur Inage.\n4. Forward this to @HagadmansaChat.__")
                os.remove("picsum.jpg")
                    
        else:
            await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**OUTPUT:**\n`Third argument must be 'True' if need a Black & White Image or must be 1 to 10 if need a blur Image`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Pass a integer value between 1 to 10 to get blur Image.\n4. Pass 'True' in third argument to get a Black & White Image.\n5. Forward this to @HagadmansaChat.__")
        
        
    else:
        await message.reply("Something went wrong")

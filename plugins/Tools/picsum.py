import os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("picsum"))
async def picsum(bot, message):
    
    r = message.text.split(None)
    id = message.chat.id 
    
    if len(message.command) == 1:
        await message.reply("No size details provided, Read Help Menu First.")
    
    elif len(message.command) == 2:
        await message.reply("Who will provide width?")
    
    elif len(r) == 3:
        API = "https://picsum.photos"
        picsum = await message.reply("`Processing...`")
        height = message.text.split(None, 2)[1]
        width = message.text.split(None, 2)[2]
        try:
            response = requests.get(f"{API}/{height}/{width}")
            open(f"{id}.jpg", "wb").write(response.content)
            await message.reply_photo(f"{id}.jpg")
            await picsum.delete()
            os.remove(f"{id}.jpg")
        except Exception as e:
            await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Forward this to @HagadmansaChat.__")
            os.remove(f"{id}.jpg")
    
    elif len(r) == 4:
        API = "https://picsum.photos"
        picsum = await message.reply("`Processing...`")
        height = message.text.split(None, 3)[1]
        width = message.text.split(None, 3)[2]
        third = message.text.split(None, 3)[3]
        
        if third == "Gray":
            try:     
                response = requests.get(f"{API}/{height}/{width}?grayscale")
                open(f"{id}.jpg", "wb").write(response.content)
                await message.reply_photo(f"{id}.jpg")
                await picsum.delete()
                os.remove(f"{id}.jpg")
            except Exception as e:
                await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Pass 'True' in thirt argument to get a Black & White Image.\n4. Forward this to @HagadmansaChat.__")
                os.remove(f"{id}.jpg")
                
        elif third == "Blur":
            try:     
                response = requests.get(f"{API}/{height}/{width}/?blur")
                open(f"{id}.jpg", "wb").write(response.content)
                await message.reply_photo(f"{id}.jpg")
                await picsum.delete()
                os.remove(f"{id}.jpg")
            except Exception as e:
                await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`{e}`\n\n**TIPS:**\n__1. Size must be in numbers.\n2. Size must be less than or equal to 5000.\n3. Pass 'Blur' in thirt argument to get blurred Image.\n4. Forward this to @HagadmansaChat.__")
                os.remove(f"{id}.jpg")
                    
        else:
            await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [105 THIRD_ARGUMENT_INVALID] - Third argument must be 'Blur' or 'Gray' (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass 'Blur' in third argument to get a Blurred Image.\n2. Pass 'Gray' in third argument to get a Black & White Image.__")
        
        
    else:
        await message.reply("Something went wrong")
        
    
    
    
    

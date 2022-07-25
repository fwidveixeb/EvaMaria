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
        except Exception:
            if height > 5000 or width > 5000:
                await picsum.edit("Size must be less than or eqaul 5000.")
                os.remove("picsum.jpg")
            else:
                await picsum.edit("Size must be in numbers.")
                os.remove("picsum.jpg")
    
    else:
        await message.reply("Something went wrong")

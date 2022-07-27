import os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("picsum"))
async def picsum(bot, message):
    
    r = message.text.split(None)
    id = message.chat.id 
    he = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "1100", "1200", "1300", "1400", "1500", "1600", "1700", "1800", "1900", "2000", "2100", "2200", "2300", "2400", "2500", "2600", "2700", "2800", "2900", "3000", "3100", "3200", "3300", "3400", "3500", "3600", "3700", "3800", "3900", "4000", "4100", "4200", "4300", "4400", "4500",  "4600", "4700", "4800", "4900", "5000"]
    wi = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "1100", "1200", "1300", "1400", "1500", "1600", "1700", "1800", "1900", "2000", "2100", "2200", "2300", "2400", "2500", "2600", "2700", "2800", "2900", "3000", "3100", "3200", "3300", "3400", "3500", "3600", "3700", "3800", "3900", "4000", "4100", "4200", "4300", "4400", "4500",  "4600", "4700", "4800", "4900", "5000"]
    
    if len(message.command) == 1:
        await message.reply("No size details provided, Read Help Menu to know how command works.")
    
    elif len(message.command) == 2:
        await message.reply("No Width provided, Read Help Menu to know how command works.")
    
    elif len(r) == 3:
        API = "https://picsum.photos"
        picsum = await message.reply("`Processing...`")
        height = message.text.split(None, 2)[1]
        width = message.text.split(None, 2)[2]
        if height not in he:
            return await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [103 FIRST_ARGUMENT_INVALID] - Height must be in multiples of 100 and should not exceed 5000 (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass Height value in multiples of 100 like 200, 500, 2500 but it should not exceed 5000.__")
        if width not in wi:
            return await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [107 SECOND_ARGUMENT_INVALID] - Width must be in multiples of 100 and should not exceed 5000 (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass Width value in multiples of 100 like 200, 500, 2500 but it should not exceed 5000.__")
        response = requests.get(f"{API}/{width}/{height}")
        open(f"picsum_{id}.jpg", "wb").write(response.content)
        await message.reply_photo(f"picsum_{id}.jpg")
        await message.reply_document(f"picsum_{id}.jpg")
        await picsum.delete()
        os.remove(f"picsum_{id}.jpg")
        
    elif len(r) == 4:
        API = "https://picsum.photos"
        picsum = await message.reply("`Processing...`")
        height = message.text.split(None, 3)[1]
        width = message.text.split(None, 3)[2]
        third = message.text.split(None, 3)[3]
        
        if third == "Gray":
            if height not in he:
                return await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [103 FIRST_ARGUMENT_INVALID] - Height must be in multiples of 100 and should not exceed 5000 (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass Height value in multiples of 100 like 200, 500, 2500 but it should not exceed 5000.__")
            if width not in wi:
                return await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [107 SECOND_ARGUMENT_INVALID] - Width must be in multiples of 100 and should not exceed 5000 (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass Width value in multiples of 100 like 200, 500, 2500 but it should not exceed 5000.__")
            response = requests.get(f"{API}/{width}/{height}?grayscale")
            open(f"picsum_{id}.jpg", "wb").write(response.content)
            await message.reply_photo(f"picsum_{id}.jpg")
            await message.reply_document(f"picsum_{id}.jpg")
            await picsum.delete()
            os.remove(f"picsum_{id}.jpg")
                
        elif third == "Blur":
            if height not in he:
                return await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [103 FIRST_ARGUMENT_INVALID] - Height must be in multiples of 100 and should not exceed 5000 (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass Height value in multiples of 100 like 200, 500, 2500 but it should not exceed 5000.__")
            if width not in wi:
                return await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [107 SECOND_ARGUMENT_INVALID] - Width must be in multiples of 100 and should not exceed 5000 (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass Width value in multiples of 100 like 200, 500, 2500 but it should not exceed 5000.__")
            response = requests.get(f"{API}/{width}/{height}/?blur")
            open(f"picsum_{id}.jpg", "wb").write(response.content)
            await message.reply_photo(f"picsum_{id}.jpg")
            await message.reply_document(f"picsum_{id}.jpg")
            await picsum.delete()
            os.remove(f"picsum_{id}.jpg")           
                    
        else:
            await picsum.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [111 THIRD_ARGUMENT_INVALID] - Third argument must be 'Blur' or 'Gray' (Caused by 'Argument.ValueError')`\n\n**TIPS:**\n__1. Pass 'Blur' in third argument to get a Blurred Image.\n2. Pass 'Gray' in third argument to get a Black & White Image.__")
       
    else:
        await message.reply("Argument limit exceeded, Read Help Menu to know how command works.")    

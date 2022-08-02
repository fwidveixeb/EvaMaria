import random
import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto

@Client.on_message(filters.command("pexels"))
async def pexels(bot, message):
  
    pexels = await message.reply("`Processing...`")
    pio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    if len(message.command) == 1:
      return await pexels.edit("No query provided for Pexels, Read Help Menu to know how command works")
    
    if len(message.command) > 1:
        nila = []
        pila = []
        query = message.command[1:]
        page = random.choice(pio)
        headers = {"Authorization": "563492ad6f917000010000012032e1a0072048019af02d2c9730b360"}
        pani = requests.get(f"https://api.pexels.com/v1/search?page={page}&query={query}", headers=headers).json()
        try:
            no_result = pani["total_results"]
            return await pexels.edit("No Results Found for your query.")
        except:
            pass
        for x in range(10):
            try:
                photo = pani["photos"][x]["src"]["large2x"]
                caption = pani["photos"][x]["alt"]
            except IndexError:
                return await pexels.edit("There is something wrong in your query, please try a different one.")
            nila.append(photo)
            pila.append(caption)
        media = [InputMediaPhoto(nila[0], caption=pila[0]), InputMediaPhoto(nila[1], caption=pila[1]), InputMediaPhoto(nila[2], caption=pila[2]), InputMediaPhoto(nila[3], caption=pila[3]), InputMediaPhoto(nila[4], caption=pila[4]), InputMediaPhoto(nila[5], caption=pila[5]), InputMediaPhoto(nila[6], caption=pila[6]), InputMediaPhoto(nila[7], caption=pila[7]), InputMediaPhoto(nila[8], caption=pila[8]), InputMediaPhoto(nila[9], caption=pila[9])]
        await message.reply_media_group(media=media)
        return await pexels.delete()

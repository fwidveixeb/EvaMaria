import os
import json
import asyncio
import traceback
from helper import randomName
from pyrogram import Client, filters
from plugins.Helper.humanbytes import humanbytes
from helper import getNew, fileId, fileSize, fileName

CHAT = -1001504830917

@Client.on_message(filters.command("link"))
async def spacebin(bot, message):
    
    if message.from_user.id not in [1250003833, 5099088450]:
        return
    
    replied = message.reply_to_message
  
    if replied:
        try:
            await message.delete()
            rn = randomName() + ".json"
            outList = []
            for x in range(1):
                outList.append({'Id': fileId(replied), 'name': fileName(replied), 'size ': humanbytes(fileSize(replied)), 'caption': replied.caption}) 
            with open(rn, "w+") as out:
                json.dump(outList, out)
            mm = await bot.send_document(CHAT, rn)
            nn = await message.reply(text=f'https://t.me/HagadmansaBot?start={getNew(fileId(mm))[0]}', disable_web_page_preview=True)
            await mm.delete()
            await asyncio.sleep(10)
            await nn.delete()
            os.remove(rn)
        except Exception as e:
            txt = traceback.format_exc() 
            return await message.reply(f"**Traceback Info:**\n`{txt}`\n**Error Text:**\n`{e}`")
    else:
        return

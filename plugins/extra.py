import asyncio
from pyrogram import Client, filters

@Client.on_message(filters.chat(-1001541636745) & filters.document & filters.video & filters.audio)
async def autoddfs(bot, message):
  dd = await message.reply(text='/dd', quote=True)
  await asyncio.sleep(0.5)
  await dd.delete()
  await asyncio.sleep(0.5)
  fs = await message.reply(text='/fs', quote=True)
  await asyncio.sleep(0.5)
  await fs.delete()

import asyncio
from pyrogram import Client, filters

@Client.on_message(filters.command('cmds'))
async def cmds(bot, message):
  
  cmds = await message.reply("`Processing...`")
  await asyncio.sleep(0.5)
  await cmds.edit('[Here](https://telegra.ph/Commands-of-Hagadmansa-Bot-08-05) are my all commands.')

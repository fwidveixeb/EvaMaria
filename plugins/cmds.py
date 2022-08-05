import asyncio
from pyrogram import Client

@Client.on_message(filters.command('cmds'))
async def cmds(bot, message):
  
  cmds = await message.reply("`Processing...`")
  await asyncio.sleep(0.5)
  await cmds.edit(
    text='[Here](https://telegra.ph/Commands-of-Hagadmansa-Bot-08-05) are my all commands.',
    disable_web_page_preview=True
  )

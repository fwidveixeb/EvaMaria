from info import ADMINS
from pyrogram import Client, filters

@Bot.on_message(filters.command('wp') & filters.user(ADMINS))
async def wp(bt, msg):
  
  wp = await message.reply('Process Started.')
  first = await Bot.ask(chat.id, "Send me first text")
  first_text = first.txt
  second = await Bot.ask(chat.id, "Send me second text")
  second_text = second.txt
  final = first_text + second_text
  await wp.edit(final)

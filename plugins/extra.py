from pyrogram import Client, filters

@Client.on_message(filters.text & filters.private, group=1)
async def echo_reversed(client, message):
    await message.reply(message.text[::1])
    
@Client.on_edited_message(filters.text & filters.photo)
async def text_and_photo(bot, message):
  await message.reply('Why you edited the message?')

@Client.on_deleted_messages(filters.text & filters.photo)
async def ndndjencue(bot, message):
  await message.reply('why you deleted message?')

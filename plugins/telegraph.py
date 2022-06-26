import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery)

@Client.on_message(filters.photo & filters.private & filters.command("telegraph"))
async def uploadphoto(client, message):
  replied = message.reply_to_message
  if not replied:
   return await message.reply('Reply to a photo to upload it on Telegra.ph.')
  file_type = replied.media
  if file_type not in ['image']:
   return await message.reply("Reply to a photo to upload it on Telegra.ph.")
  msg = await message.reply_text("Trying to download the photo...")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message.reply_to_message, file_name=img_path)
  await msg.edit_text("Now trying to Upload it on Telegra.ph.")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("Something went wrong.") 
  else:
    await msg.edit_text(
      text=f"Here is your link:- https://telegra.ph{tlink[0]}",
      disable_web_page_preview=True)     
    os.remove(img_path) 
